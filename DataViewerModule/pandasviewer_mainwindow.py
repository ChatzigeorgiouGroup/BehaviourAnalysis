# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pandasviewer_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.AllColumns = QtWidgets.QWidget()
        self.AllColumns.setObjectName("AllColumns")
        self.gridLayout = QtWidgets.QGridLayout(self.AllColumns)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonAddToSelection = QtWidgets.QPushButton(self.AllColumns)
        self.pushButtonAddToSelection.setObjectName("pushButtonAddToSelection")
        self.gridLayout.addWidget(self.pushButtonAddToSelection, 2, 0, 1, 1)
        self.listWidgetAllColumns = QtWidgets.QListWidget(self.AllColumns)
        self.listWidgetAllColumns.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidgetAllColumns.setObjectName("listWidgetAllColumns")
        self.gridLayout.addWidget(self.listWidgetAllColumns, 0, 0, 1, 1)
        self.treeWidgetAllColums = QtWidgets.QTreeWidget(self.AllColumns)
        self.treeWidgetAllColums.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidgetAllColums.setObjectName("treeWidgetAllColums")
        self.treeWidgetAllColums.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidgetAllColums, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.AllColumns, "")
        self.SelectedColumns = QtWidgets.QWidget()
        self.SelectedColumns.setObjectName("SelectedColumns")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.SelectedColumns)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidgetSelectedColumns = QtWidgets.QListWidget(self.SelectedColumns)
        self.listWidgetSelectedColumns.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidgetSelectedColumns.setObjectName("listWidgetSelectedColumns")
        self.gridLayout_4.addWidget(self.listWidgetSelectedColumns, 0, 0, 1, 1)
        self.pushButtonRemoveFromSelection = QtWidgets.QPushButton(self.SelectedColumns)
        self.pushButtonRemoveFromSelection.setObjectName("pushButtonRemoveFromSelection")
        self.gridLayout_4.addWidget(self.pushButtonRemoveFromSelection, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.SelectedColumns, "")
        self.RowFilters = QtWidgets.QWidget()
        self.RowFilters.setObjectName("RowFilters")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.RowFilters)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBoxSelectedColumns = QtWidgets.QComboBox(self.RowFilters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSelectedColumns.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectedColumns.setSizePolicy(sizePolicy)
        self.comboBoxSelectedColumns.setObjectName("comboBoxSelectedColumns")
        self.horizontalLayout_2.addWidget(self.comboBoxSelectedColumns)
        self.checkBoxUnique = QtWidgets.QCheckBox(self.RowFilters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxUnique.sizePolicy().hasHeightForWidth())
        self.checkBoxUnique.setSizePolicy(sizePolicy)
        self.checkBoxUnique.setObjectName("checkBoxUnique")
        self.horizontalLayout_2.addWidget(self.checkBoxUnique)
        self.checkBoxSorting = QtWidgets.QCheckBox(self.RowFilters)
        self.checkBoxSorting.setObjectName("checkBoxSorting")
        self.horizontalLayout_2.addWidget(self.checkBoxSorting)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidgetUniqueValues = QtWidgets.QListWidget(self.RowFilters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.listWidgetUniqueValues.sizePolicy().hasHeightForWidth())
        self.listWidgetUniqueValues.setSizePolicy(sizePolicy)
        self.listWidgetUniqueValues.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidgetUniqueValues.setObjectName("listWidgetUniqueValues")
        self.verticalLayout.addWidget(self.listWidgetUniqueValues)
        self.label_4 = QtWidgets.QLabel(self.RowFilters)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.listWidgetAppliedFilters = QtWidgets.QListWidget(self.RowFilters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetAppliedFilters.sizePolicy().hasHeightForWidth())
        self.listWidgetAppliedFilters.setSizePolicy(sizePolicy)
        self.listWidgetAppliedFilters.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidgetAppliedFilters.setObjectName("listWidgetAppliedFilters")
        self.verticalLayout.addWidget(self.listWidgetAppliedFilters)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonInclude = QtWidgets.QRadioButton(self.RowFilters)
        self.radioButtonInclude.setChecked(True)
        self.radioButtonInclude.setObjectName("radioButtonInclude")
        self.horizontalLayout.addWidget(self.radioButtonInclude)
        self.radioButtonLessThan = QtWidgets.QRadioButton(self.RowFilters)
        self.radioButtonLessThan.setObjectName("radioButtonLessThan")
        self.horizontalLayout.addWidget(self.radioButtonLessThan)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBoxPreviewSelection = QtWidgets.QCheckBox(self.RowFilters)
        self.checkBoxPreviewSelection.setObjectName("checkBoxPreviewSelection")
        self.horizontalLayout_3.addWidget(self.checkBoxPreviewSelection)
        self.pushButtonApplyFilters = QtWidgets.QPushButton(self.RowFilters)
        self.pushButtonApplyFilters.setObjectName("pushButtonApplyFilters")
        self.horizontalLayout_3.addWidget(self.pushButtonApplyFilters)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget_2.addTab(self.RowFilters, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.AllData = QtWidgets.QWidget()
        self.AllData.setObjectName("AllData")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.AllData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidgetAllData = QtWidgets.QTableWidget(self.AllData)
        self.tableWidgetAllData.setObjectName("tableWidgetAllData")
        self.tableWidgetAllData.setColumnCount(0)
        self.tableWidgetAllData.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidgetAllData, 0, 0, 1, 1)
        self.tabWidget.addTab(self.AllData, "")
        self.SelectedData = QtWidgets.QWidget()
        self.SelectedData.setObjectName("SelectedData")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.SelectedData)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidgetSelectedData = QtWidgets.QTableWidget(self.SelectedData)
        self.tableWidgetSelectedData.setObjectName("tableWidgetSelectedData")
        self.tableWidgetSelectedData.setColumnCount(0)
        self.tableWidgetSelectedData.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidgetSelectedData, 0, 0, 1, 1)
        self.tabWidget.addTab(self.SelectedData, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.groupBoxPlotting = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPlotting.sizePolicy().hasHeightForWidth())
        self.groupBoxPlotting.setSizePolicy(sizePolicy)
        self.groupBoxPlotting.setObjectName("groupBoxPlotting")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBoxPlotting)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frameTransform = QtWidgets.QFrame(self.groupBoxPlotting)
        self.frameTransform.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTransform.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTransform.setObjectName("frameTransform")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frameTransform)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.comboBoxTransformations = QtWidgets.QComboBox(self.frameTransform)
        self.comboBoxTransformations.setObjectName("comboBoxTransformations")
        self.gridLayout_7.addWidget(self.comboBoxTransformations, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButtonAddTransformToData = QtWidgets.QPushButton(self.frameTransform)
        self.pushButtonAddTransformToData.setObjectName("pushButtonAddTransformToData")
        self.horizontalLayout_7.addWidget(self.pushButtonAddTransformToData)
        self.pushButtonTransformData = QtWidgets.QPushButton(self.frameTransform)
        self.pushButtonTransformData.setObjectName("pushButtonTransformData")
        self.horizontalLayout_7.addWidget(self.pushButtonTransformData)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frameTransform)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frameTransform, 0, 1, 1, 1)
        self.framePlotWidget = QtWidgets.QFrame(self.groupBoxPlotting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePlotWidget.sizePolicy().hasHeightForWidth())
        self.framePlotWidget.setSizePolicy(sizePolicy)
        self.framePlotWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePlotWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePlotWidget.setObjectName("framePlotWidget")
        self.gridLayout_9.addWidget(self.framePlotWidget, 3, 0, 1, 2)
        self.framePlotControls = QtWidgets.QFrame(self.groupBoxPlotting)
        self.framePlotControls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePlotControls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePlotControls.setObjectName("framePlotControls")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.framePlotControls)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.framePlotControls)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBoxXData = QtWidgets.QComboBox(self.framePlotControls)
        self.comboBoxXData.setObjectName("comboBoxXData")
        self.verticalLayout_3.addWidget(self.comboBoxXData)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.framePlotControls)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBoxYData = QtWidgets.QComboBox(self.framePlotControls)
        self.comboBoxYData.setObjectName("comboBoxYData")
        self.verticalLayout_2.addWidget(self.comboBoxYData)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.framePlotControls)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.gridLayout_8.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboBoxPlotType = QtWidgets.QComboBox(self.framePlotControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPlotType.sizePolicy().hasHeightForWidth())
        self.comboBoxPlotType.setSizePolicy(sizePolicy)
        self.comboBoxPlotType.setObjectName("comboBoxPlotType")
        self.horizontalLayout_5.addWidget(self.comboBoxPlotType)
        self.labelColorParam = QtWidgets.QLabel(self.framePlotControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelColorParam.sizePolicy().hasHeightForWidth())
        self.labelColorParam.setSizePolicy(sizePolicy)
        self.labelColorParam.setObjectName("labelColorParam")
        self.horizontalLayout_5.addWidget(self.labelColorParam)
        self.comboBoxColorParam = QtWidgets.QComboBox(self.framePlotControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxColorParam.sizePolicy().hasHeightForWidth())
        self.comboBoxColorParam.setSizePolicy(sizePolicy)
        self.comboBoxColorParam.setObjectName("comboBoxColorParam")
        self.horizontalLayout_5.addWidget(self.comboBoxColorParam)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.pushButtonPlot = QtWidgets.QPushButton(self.framePlotControls)
        self.pushButtonPlot.setObjectName("pushButtonPlot")
        self.gridLayout_8.addWidget(self.pushButtonPlot, 3, 0, 1, 1)
        self.gridLayout_9.addWidget(self.framePlotControls, 0, 0, 2, 1)
        self.frameStatistics = QtWidgets.QFrame(self.groupBoxPlotting)
        self.frameStatistics.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStatistics.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameStatistics.setObjectName("frameStatistics")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frameStatistics)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_7 = QtWidgets.QLabel(self.frameStatistics)
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)
        self.doubleSpinBoxAlpha = QtWidgets.QDoubleSpinBox(self.frameStatistics)
        self.doubleSpinBoxAlpha.setDecimals(3)
        self.doubleSpinBoxAlpha.setSingleStep(0.01)
        self.doubleSpinBoxAlpha.setProperty("value", 0.05)
        self.doubleSpinBoxAlpha.setObjectName("doubleSpinBoxAlpha")
        self.gridLayout_10.addWidget(self.doubleSpinBoxAlpha, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frameStatistics)
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBoxStatisticalTests = QtWidgets.QComboBox(self.frameStatistics)
        self.comboBoxStatisticalTests.setObjectName("comboBoxStatisticalTests")
        self.gridLayout_10.addWidget(self.comboBoxStatisticalTests, 0, 1, 1, 1)
        self.pushButtonTest = QtWidgets.QPushButton(self.frameStatistics)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.gridLayout_10.addWidget(self.pushButtonTest, 3, 0, 1, 2)
        self.lineEditPvalue = QtWidgets.QLineEdit(self.frameStatistics)
        self.lineEditPvalue.setObjectName("lineEditPvalue")
        self.gridLayout_10.addWidget(self.lineEditPvalue, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frameStatistics)
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 4, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frameStatistics, 1, 1, 1, 1)
        self.frameConsole = QtWidgets.QFrame(self.groupBoxPlotting)
        self.frameConsole.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameConsole.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConsole.setObjectName("frameConsole")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameConsole)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelConsole = QtWidgets.QLabel(self.frameConsole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelConsole.sizePolicy().hasHeightForWidth())
        self.labelConsole.setSizePolicy(sizePolicy)
        self.labelConsole.setObjectName("labelConsole")
        self.horizontalLayout_6.addWidget(self.labelConsole)
        self.pushButtonCloseConsole = QtWidgets.QPushButton(self.frameConsole)
        self.pushButtonCloseConsole.setObjectName("pushButtonCloseConsole")
        self.horizontalLayout_6.addWidget(self.pushButtonCloseConsole)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout_9.addWidget(self.frameConsole, 4, 0, 1, 2)
        self.gridLayout_5.addWidget(self.groupBoxPlotting, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 30))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSave_Selected_Data = QtWidgets.QMenu(self.menuTools)
        self.menuSave_Selected_Data.setObjectName("menuSave_Selected_Data")
        self.menuStatistiscs = QtWidgets.QMenu(self.menuTools)
        self.menuStatistiscs.setObjectName("menuStatistiscs")
        self.menuNormalize_Selected_Data = QtWidgets.QMenu(self.menuTools)
        self.menuNormalize_Selected_Data.setObjectName("menuNormalize_Selected_Data")
        self.menuFeatures = QtWidgets.QMenu(self.menuTools)
        self.menuFeatures.setObjectName("menuFeatures")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_as_CSV = QtWidgets.QAction(MainWindow)
        self.action_as_CSV.setObjectName("action_as_CSV")
        self.action_as_Pickle = QtWidgets.QAction(MainWindow)
        self.action_as_Pickle.setObjectName("action_as_Pickle")
        self.actionLoad_Dataset_into_Viewer = QtWidgets.QAction(MainWindow)
        self.actionLoad_Dataset_into_Viewer.setObjectName("actionLoad_Dataset_into_Viewer")
        self.actionopen_console = QtWidgets.QAction(MainWindow)
        self.actionopen_console.setObjectName("actionopen_console")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionPlotting = QtWidgets.QAction(MainWindow)
        self.actionPlotting.setObjectName("actionPlotting")
        self.actionConsole = QtWidgets.QAction(MainWindow)
        self.actionConsole.setObjectName("actionConsole")
        self.actionData_Selection = QtWidgets.QAction(MainWindow)
        self.actionData_Selection.setObjectName("actionData_Selection")
        self.actionReciprocal = QtWidgets.QAction(MainWindow)
        self.actionReciprocal.setObjectName("actionReciprocal")
        self.actionReciprocal_Square_Root = QtWidgets.QAction(MainWindow)
        self.actionReciprocal_Square_Root.setObjectName("actionReciprocal_Square_Root")
        self.actionNatural_Logarithm = QtWidgets.QAction(MainWindow)
        self.actionNatural_Logarithm.setObjectName("actionNatural_Logarithm")
        self.actionSquare_Root = QtWidgets.QAction(MainWindow)
        self.actionSquare_Root.setObjectName("actionSquare_Root")
        self.actionTransforms = QtWidgets.QAction(MainWindow)
        self.actionTransforms.setObjectName("actionTransforms")
        self.actionScan_for_significance = QtWidgets.QAction(MainWindow)
        self.actionScan_for_significance.setObjectName("actionScan_for_significance")
        self.actionStatistics = QtWidgets.QAction(MainWindow)
        self.actionStatistics.setObjectName("actionStatistics")
        self.actionRename_items_in_column = QtWidgets.QAction(MainWindow)
        self.actionRename_items_in_column.setObjectName("actionRename_items_in_column")
        self.actionPairwaise_Test_Categorical = QtWidgets.QAction(MainWindow)
        self.actionPairwaise_Test_Categorical.setObjectName("actionPairwaise_Test_Categorical")
        self.actionminmax_scale = QtWidgets.QAction(MainWindow)
        self.actionminmax_scale.setObjectName("actionminmax_scale")
        self.actionmean_scale = QtWidgets.QAction(MainWindow)
        self.actionmean_scale.setObjectName("actionmean_scale")
        self.actionRoaming = QtWidgets.QAction(MainWindow)
        self.actionRoaming.setObjectName("actionRoaming")
        self.menuSave_Selected_Data.addAction(self.action_as_CSV)
        self.menuSave_Selected_Data.addAction(self.action_as_Pickle)
        self.menuStatistiscs.addAction(self.actionScan_for_significance)
        self.menuStatistiscs.addAction(self.actionPairwaise_Test_Categorical)
        self.menuNormalize_Selected_Data.addAction(self.actionminmax_scale)
        self.menuNormalize_Selected_Data.addAction(self.actionmean_scale)
        self.menuFeatures.addAction(self.actionRoaming)
        self.menuTools.addAction(self.actionLoad_Dataset_into_Viewer)
        self.menuTools.addAction(self.menuSave_Selected_Data.menuAction())
        self.menuTools.addAction(self.actionRename_items_in_column)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuFeatures.menuAction())
        self.menuTools.addAction(self.menuStatistiscs.menuAction())
        self.menuTools.addAction(self.menuNormalize_Selected_Data.menuAction())
        self.menuView.addAction(self.actionData_Selection)
        self.menuView.addAction(self.actionData)
        self.menuView.addAction(self.actionPlotting)
        self.menuView.addAction(self.actionConsole)
        self.menuView.addAction(self.actionTransforms)
        self.menuView.addAction(self.actionStatistics)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Data Selection"))
        self.pushButtonAddToSelection.setText(_translate("MainWindow", "Add to Selection"))
        self.listWidgetAllColumns.setSortingEnabled(False)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.AllColumns), _translate("MainWindow", "All Columns"))
        self.pushButtonRemoveFromSelection.setText(_translate("MainWindow", "Remove from Selection"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.SelectedColumns), _translate("MainWindow", "Selected Columns"))
        self.checkBoxUnique.setText(_translate("MainWindow", "Unique vals"))
        self.checkBoxSorting.setText(_translate("MainWindow", "Sort"))
        self.label_4.setText(_translate("MainWindow", "Applied Filters:"))
        self.radioButtonInclude.setText(_translate("MainWindow", "include"))
        self.radioButtonLessThan.setText(_translate("MainWindow", "exclude"))
        self.checkBoxPreviewSelection.setText(_translate("MainWindow", "Preview Selection"))
        self.pushButtonApplyFilters.setText(_translate("MainWindow", "Apply"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.RowFilters), _translate("MainWindow", "Row Filters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AllData), _translate("MainWindow", "All Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SelectedData), _translate("MainWindow", "Selected Data"))
        self.groupBoxPlotting.setTitle(_translate("MainWindow", "Plotting and Stats"))
        self.pushButtonAddTransformToData.setText(_translate("MainWindow", "Add to data"))
        self.pushButtonTransformData.setText(_translate("MainWindow", "View Transformation"))
        self.label_5.setText(_translate("MainWindow", "Data Transformation"))
        self.label_2.setText(_translate("MainWindow", "X-Data"))
        self.label.setText(_translate("MainWindow", "Y-Data"))
        self.label_3.setText(_translate("MainWindow", "Plot Type"))
        self.labelColorParam.setText(_translate("MainWindow", "Color by:"))
        self.pushButtonPlot.setText(_translate("MainWindow", "Plot"))
        self.frameStatistics.setToolTip(_translate("MainWindow", "<html><head/><body><p>CAUTION:</p><p><br/></p><p>The  test is performed on data selected for the plot. If you want to test a transformed parameter, add it to data first, and then plot it. Otherwise you might not be testing what you think you are testing. </p><p><br/></p><p>Only kruskal-wallis and one-way anova are implemented, and these are not suitable for comparing a dataset of only two groups. </p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Alpha"))
        self.label_6.setText(_translate("MainWindow", "Test"))
        self.pushButtonTest.setText(_translate("MainWindow", "Test"))
        self.label_8.setText(_translate("MainWindow", "pval:"))
        self.labelConsole.setText(_translate("MainWindow", "Python Console:"))
        self.pushButtonCloseConsole.setText(_translate("MainWindow", "close"))
        self.menuTools.setTitle(_translate("MainWindow", "Too&ls"))
        self.menuSave_Selected_Data.setTitle(_translate("MainWindow", "&Save Selected Data..."))
        self.menuStatistiscs.setTitle(_translate("MainWindow", "Stat&istiscs"))
        self.menuNormalize_Selected_Data.setTitle(_translate("MainWindow", "&Normalize Selected Data"))
        self.menuFeatures.setTitle(_translate("MainWindow", "Features"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.action_as_CSV.setText(_translate("MainWindow", "...as &CSV"))
        self.action_as_Pickle.setText(_translate("MainWindow", "...as &Pickle"))
        self.actionLoad_Dataset_into_Viewer.setText(_translate("MainWindow", "&Load Dataset into Viewer"))
        self.actionopen_console.setText(_translate("MainWindow", "Console"))
        self.actionData.setText(_translate("MainWindow", "&Data"))
        self.actionPlotting.setText(_translate("MainWindow", "&Plotting"))
        self.actionConsole.setText(_translate("MainWindow", "&Console"))
        self.actionData_Selection.setText(_translate("MainWindow", "&Selection Tools"))
        self.actionReciprocal.setText(_translate("MainWindow", "Reciprocal"))
        self.actionReciprocal_Square_Root.setText(_translate("MainWindow", "Reciprocal Square Root"))
        self.actionNatural_Logarithm.setText(_translate("MainWindow", "Natural Logarithm"))
        self.actionSquare_Root.setText(_translate("MainWindow", "Square Root"))
        self.actionTransforms.setText(_translate("MainWindow", "&Transforms"))
        self.actionScan_for_significance.setText(_translate("MainWindow", "&Scan Categoricals"))
        self.actionStatistics.setText(_translate("MainWindow", "Stat&istics"))
        self.actionRename_items_in_column.setText(_translate("MainWindow", "&Rename items in column"))
        self.actionPairwaise_Test_Categorical.setText(_translate("MainWindow", "&Barcodes and Pairwise Testing"))
        self.actionminmax_scale.setText(_translate("MainWindow", "&minmax_scale"))
        self.actionminmax_scale.setToolTip(_translate("MainWindow", "Forces data to the range [-1,1]"))
        self.actionmean_scale.setText(_translate("MainWindow", "mean_&scale"))
        self.actionmean_scale.setToolTip(_translate("MainWindow", "<html><head/><body><p>Standardizes.<br/>Forces zero mean and unit variance so that for each feature:</p><p>mean = 0,<br/>std = 1.0.</p></body></html>"))
        self.actionRoaming.setText(_translate("MainWindow", "Roaming"))


