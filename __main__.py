# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:50:02 2018

@author: install
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:20:50 2018

@author: ddo003
"""

from mainwindow import Ui_MainWindow
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets, uic
import pyqtgraph
import sys, os, shutil
from distutils.dir_util import copy_tree
from tqdm import tqdm
from supportclasses import DataHandler, WaitingThread
from CenterfinderModule.CenterFindingWindow import CenterFindingWindow
from CenterfinderModule.CenterFinder import Centerfinder
from DataViewer import DataViewer
from threading import Thread

import psutil
import time
##Load creatorfile and 
#qtCreatorFile = "mainwindow.ui" # Enter file here. 
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
# 
#from mainwindow import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
    
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/centerfinder.png"))
        self.project_path = None
        self.ui.menuTools.setEnabled(False)

        self.ui.tabWidgetFolders.currentChanged.connect(self.update_tree)

        self.ui.actionNew_Project.triggered.connect(self.new_project)
        self.ui.actionScrape_New_Data.triggered.connect(self.scrape_new_data)

        self.ui.treeWidgetDataFolder.itemDoubleClicked.connect(self.item_double_clicked)
        self.ui.treeWidgetProjectFolder.itemDoubleClicked.connect(self.item_double_clicked)

        self.ui.actionCenterfinding_All.triggered.connect(lambda: self.open_centerfinding_window(mode = "all"))
        self.ui.actionCenterfinding_selection.triggered.connect(lambda: self.open_centerfinding_window(mode="selection"))
        

        self.ui.actionParameters_and_Metadata_for_all.triggered.connect(lambda: self.calculate_parameters(mode = "all"))
        self.ui.actionParameters_for_selection.triggered.connect(lambda: self.calculate_parameters(mode = "selection"))
        self.ui.actionMissing_Parameter.triggered.connect(lambda: self.calculate_parameters(mode = "missing"))
        self.ui.actionOnly_Metadata.triggered.connect(self.calculate_metadata)
        self.ui.actionLoad_Project.triggered.connect(self.load_project)
        self.ui.actionLoad_Existing_Dataset.triggered.connect(self.load_project_to_add)

    def load_project(self):
        self.project_path = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose a project to load")
        self.update_tree()
        self.ui.menuTools.setEnabled(True)
        self.ui.actionNew_Project.setEnabled(False)

    def new_project(self):
        self.project_path = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose a new project path")

        self.scrape_new_data()
        self.ui.menuTools.setEnabled(True)
        self.ui.actionNew_Project.setEnabled(False)

    def scrape_new_data(self):
        if not os.path.exists(os.path.join(self.project_path, "dataframes")):
            os.mkdir(os.path.join(self.project_path, "dataframes"))
        self.data_path = QtWidgets.QFileDialog.getExistingDirectory(caption="Select Data Folder")
        self.display_folder_structure(self.data_path, self.ui.treeWidgetDataFolder)
        t = Thread(target=self._new_project)
        t.start()
        self.display_folder_structure(self.project_path, self.ui.treeWidgetProjectFolder)
        self.display_folder_structure(self.data_path, self.ui.treeWidgetDataFolder)

    def copy_data_to_project(self, new_path):
        sys.stdout.write("\n Copying new data to project folder.\n")
        copy_tree(new_path, self.project_path, update=True)
        sys.stdout.write("\n Done Copying \n")

    def load_project_to_add(self):
        if not self.project_path:
            QtWidgets.QMessageBox.warning(self, "No Project path defined",
                                          "Select a project path before selecting a project to load")
            self.project_path = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose a project path")
        new_data_path = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose a project to load")

        t = Thread(target = self.copy_data_to_project, args = (new_data_path,))
        t.start()
        while t.isAlive():
            sys.stdout.write(".")
            time.sleep(0.2)
        self.update_tree()
        self.ui.menuTools.setEnabled(True)
        self.ui.actionNew_Project.setEnabled(False)

    def _new_project(self):
        dirs = [root for root, dirs, files in os.walk(self.data_path) if
                ".avi" in " ".join(files) and "metadata.txt" in " ".join(files)]

        for d in tqdm(dirs):
            try:

                #check if files are in the folders
                stimuli_profile = "None"
                metadata = "None"
                temperature = "None"
                arena = "None"
                tracking = "None"
                for root, directories, files in os.walk(d):
                    for f in files:
                        if "stimuli_profile" in f:
                            stimuli_profile = os.path.join(root, f)
                        elif "metadata" in f:
                            metadata = os.path.join(root, f)
                        elif "temperature" in f:
                            temperature = os.path.join(root, f)
                        elif "arena.txt" in f.lower():
                            arena = os.path.join(root, f)
                        elif "tracking" in f.lower() and "realspace" not in f.lower():
                            try:
                                with open(os.path.join(root, f), "r") as tracking_file_to_read:
                                    lines = tracking_file_to_read.readlines()
                                    if len(lines) <= 100:
                                        tracking = "None"

                                    else:
                                        tracking = os.path.join(root, f)
                            except:
                                tracking = "None"

                all_files_there = True
                for f in [stimuli_profile, metadata, temperature, arena, tracking]:
                    if f == "None":
                        all_files_there = False

                if all_files_there:
                    if "exp_" not in d.lower():
                        newdir = os.path.join(self.project_path, "Exp_"+d.split("\\")[-1])
                    else:
                        newdir = os.path.join(self.project_path, d.split("\\")[-1])
                    if not os.path.exists(newdir):
                        os.mkdir(newdir)
                    for f in [stimuli_profile, metadata, temperature, arena, tracking]:
                        shutil.copy2(os.path.join(root, f), newdir)
                    with open(os.path.join(newdir, "path_to_raw_data.txt"), "w") as filename:
                        filename.write(d)
                else:
                    print("\nNot all files present for ", d, "\n")
            except Exception as e:
                sys.stdout.write("\n"+e)
        self.update_tree(0)


    def update_tree(self, index=0):
        try:
            self.ui.treeWidgetProjectFolder.clear()
            self.display_folder_structure(self.project_path, self.ui.treeWidgetProjectFolder)
            files_loaded = len([x for x in os.listdir(self.project_path) if "exp" in x.lower() and  os.path.isdir(os.path.join(self.project_path,x))])
            circle_files = len([f for root, dirs, files in os.walk(self.project_path) for f in files if "center" in f.lower()])

            sys.stdout.write("Files Loaded: "+str(files_loaded)+" Center files: "+str(circle_files)+"\n")

            root = self.ui.treeWidgetProjectFolder.invisibleRootItem()
            for i in range(root.childCount()):
                item = root.child(i)
                listed_dir = " ".join(os.listdir(item.text(1)))
                if "center" in listed_dir and "dataframe" not in listed_dir:
                    item.setBackground(0, QtGui.QColor("lightyellow"))
                if "center" not in listed_dir and "dataframe" in listed_dir:
                    item.setBackground(0, QtGui.QColor("lightblue"))
                if "center" in listed_dir and "dataframe" in listed_dir:
                    item.setBackground(0, QtGui.QColor("lightgreen"))
                    
        except Exception as e:
            print(e)
            print("No paths set. This is likely not so helpful.")

    def display_folder_structure(self, path, tree):
        for element in os.listdir(path):
            path_info = os.path.join(path, element)
            parent_item = QtWidgets.QTreeWidgetItem(tree,  [os.path.basename(element)])
            parent_item.setData(1,0,path_info)

            if os.path.isdir(path_info):
                self.display_folder_structure(path_info, parent_item)
                parent_item.setIcon(0, QtGui.QIcon("icons/folder.ico"))

            else:
                if path_info.endswith(".avi"):
                    parent_item.setIcon(0, QtGui.QIcon("icons/video.ico"))

                elif path_info.endswith(".pickle"):
                    parent_item.setIcon(0, QtGui.QIcon("icons/pickle.png"))
                else:
                    parent_item.setIcon(0, QtGui.QIcon("icons/file.ico"))

    def find_center(self, path):
        cf = Centerfinder()
        circles = cf.find(path, show_result=True)
        print(circles)

    def item_double_clicked(self, item):
        text = item.text(1)
        print(text)
        try:
            if text.endswith(".avi"):
                self.find_center(text)
            elif text.endswith(".txt"):
                os.popen("notepad "+text)
            elif text.endswith(".pickle"):
                self.dv = DataViewer(df_path = text)
                self.dv.show()
        except Exception as e:
            print(e)
            print("No action connected to files with this extension")

    def open_centerfinding_window(self, mode = "all"):
        if mode == "all":
            root = self.ui.treeWidgetProjectFolder.invisibleRootItem()
            selection = [root.child(i) for i in range(root.childCount()) if root.child(i).text(0) != "dataframes"]
            
        else:
            selection = self.ui.treeWidgetProjectFolder.selectedItems()
#        self.centerfinding_window = CenterFindingWindow(data_path = self.data_path, project_path = self.project_path)

        self.centerfinding_window = CenterFindingWindow(project_path= self.project_path, selection=selection)
        self.centerfinding_window.show()

    def calculate_parameters(self, mode):
        if mode == "selection":
            selection = [item.text(1) for item in  self.ui.treeWidgetProjectFolder.selectedItems()]
            self.datahandler = DataHandler(path = self.project_path, selection= selection)
        elif mode == "missing":
            selection = []
            root = self.ui.treeWidgetProjectFolder.invisibleRootItem()
            for i in range(root.childCount()):
                item = root.child(i)
                if "dataframe" not in " ".join(os.listdir(item.text(1))):
                    selection.append(item.text(1))
            self.datahandler = DataHandler(path=self.project_path, selection=selection)
        else:
            self.datahandler = DataHandler(self.project_path)
        self.datahandler.calculate_all_parameters()
        QtWidgets.QMessageBox.warning(self, "Calculations have started", "This may take a while, and for now there is no way out. \n Keep an eye on the console for more info.")

    def calculate_metadata(self):
        self.datahandler = DataHandler(self.project_path)
        self.datahandler.gather_common_dataframe()





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Analyze")
    window.show()
#    sys.exit(app.exec_())
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
