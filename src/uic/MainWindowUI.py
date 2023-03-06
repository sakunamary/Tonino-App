# Form implementation generated from reading ui file 'ui/MainWindowUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 550)
        MainWindow.setMinimumSize(QtCore.QSize(0, 550))
        MainWindow.setWindowTitle("Tonino")
        MainWindow.setToolTip("")
        MainWindow.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, -1, 25)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setToolTip("")
        self.label_2.setAccessibleDescription("")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setText("AVG")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.LCDavg = QtWidgets.QLCDNumber(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LCDavg.sizePolicy().hasHeightForWidth())
        self.LCDavg.setSizePolicy(sizePolicy)
        self.LCDavg.setMinimumSize(QtCore.QSize(0, 25))
        self.LCDavg.setToolTip("")
        self.LCDavg.setAccessibleDescription("")
        self.LCDavg.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.LCDavg.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.LCDavg.setLineWidth(1)
        self.LCDavg.setMidLineWidth(0)
        self.LCDavg.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.LCDavg.setObjectName("LCDavg")
        self.verticalLayout_2.addWidget(self.LCDavg)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setToolTip("")
        self.label_4.setAccessibleDescription("")
        self.label_4.setText("STDEV")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.LCDstdev = QtWidgets.QLCDNumber(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LCDstdev.sizePolicy().hasHeightForWidth())
        self.LCDstdev.setSizePolicy(sizePolicy)
        self.LCDstdev.setMinimumSize(QtCore.QSize(0, 25))
        self.LCDstdev.setToolTip("")
        self.LCDstdev.setAccessibleDescription("")
        self.LCDstdev.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.LCDstdev.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.LCDstdev.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.LCDstdev.setObjectName("LCDstdev")
        self.verticalLayout_3.addWidget(self.LCDstdev)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(15, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setToolTip("")
        self.label_5.setAccessibleDescription("")
        self.label_5.setText("CONF95%")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.LCDconf = QtWidgets.QLCDNumber(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LCDconf.sizePolicy().hasHeightForWidth())
        self.LCDconf.setSizePolicy(sizePolicy)
        self.LCDconf.setMinimumSize(QtCore.QSize(0, 25))
        self.LCDconf.setToolTip("")
        self.LCDconf.setAccessibleDescription("")
        self.LCDconf.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.LCDconf.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.LCDconf.setLineWidth(1)
        self.LCDconf.setSmallDecimalPoint(False)
        self.LCDconf.setMode(QtWidgets.QLCDNumber.Mode.Bin)
        self.LCDconf.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.LCDconf.setObjectName("LCDconf")
        self.verticalLayout_5.addWidget(self.LCDconf)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(100, 0))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setToolTip("")
        self.tableView.setAccessibleDescription("")
        self.tableView.setAutoFillBackground(False)
        self.tableView.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableView)
        self.widget = mplwidget(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 300))
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdd.setToolTip("")
        self.pushButtonAdd.setAccessibleDescription("")
        self.pushButtonAdd.setText("Add")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_2.addWidget(self.pushButtonAdd)
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDelete.setToolTip("")
        self.pushButtonDelete.setAccessibleDescription("")
        self.pushButtonDelete.setText("Delete")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_2.addWidget(self.pushButtonDelete)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButtonSort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSort.setToolTip("")
        self.pushButtonSort.setAccessibleDescription("")
        self.pushButtonSort.setText("Sort")
        self.pushButtonSort.setObjectName("pushButtonSort")
        self.horizontalLayout_2.addWidget(self.pushButtonSort)
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClear.setToolTip("")
        self.pushButtonClear.setAccessibleDescription("")
        self.pushButtonClear.setText("Clear")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.pushButtonCalib = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCalib.setToolTip("")
        self.pushButtonCalib.setAccessibleDescription("")
        self.pushButtonCalib.setText("Calibrate")
        self.pushButtonCalib.setObjectName("pushButtonCalib")
        self.horizontalLayout_2.addWidget(self.pushButtonCalib)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setToolTip("")
        self.label_3.setAccessibleDescription("")
        self.label_3.setText("0")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.degreeSlider = QtWidgets.QSlider(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.degreeSlider.sizePolicy().hasHeightForWidth())
        self.degreeSlider.setSizePolicy(sizePolicy)
        self.degreeSlider.setMinimumSize(QtCore.QSize(80, 0))
        self.degreeSlider.setMaximumSize(QtCore.QSize(150, 16777215))
        self.degreeSlider.setToolTip("")
        self.degreeSlider.setAccessibleDescription("")
        self.degreeSlider.setMinimum(0)
        self.degreeSlider.setMaximum(3)
        self.degreeSlider.setPageStep(1)
        self.degreeSlider.setTracking(False)
        self.degreeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.degreeSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.degreeSlider.setTickInterval(1)
        self.degreeSlider.setObjectName("degreeSlider")
        self.horizontalLayout_5.addWidget(self.degreeSlider)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setToolTip("")
        self.label.setAccessibleDescription("")
        self.label.setText("3 ")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.pushButtonDefaults = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDefaults.setToolTip("")
        self.pushButtonDefaults.setAccessibleDescription("")
        self.pushButtonDefaults.setText("Defaults")
        self.pushButtonDefaults.setObjectName("pushButtonDefaults")
        self.horizontalLayout_2.addWidget(self.pushButtonDefaults)
        self.pushButtonUpload = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonUpload.setToolTip("")
        self.pushButtonUpload.setAccessibleDescription("")
        self.pushButtonUpload.setText("Upload")
        self.pushButtonUpload.setObjectName("pushButtonUpload")
        self.horizontalLayout_2.addWidget(self.pushButtonUpload)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.status = QtWidgets.QStatusBar(parent=MainWindow)
        self.status.setToolTip("")
        self.status.setAccessibleDescription("")
        self.status.setSizeGripEnabled(False)
        self.status.setObjectName("status")
        MainWindow.setStatusBar(self.status)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 808, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_Recent = QtWidgets.QMenu(parent=self.menuFile)
        self.menuOpen_Recent.setToolTip("")
        self.menuOpen_Recent.setAccessibleDescription("")
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")
        self.menuOpen_ApplyRecent = QtWidgets.QMenu(parent=self.menuFile)
        self.menuOpen_ApplyRecent.setToolTip("")
        self.menuOpen_ApplyRecent.setAccessibleDescription("")
        self.menuOpen_ApplyRecent.setObjectName("menuOpen_ApplyRecent")
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setText("Quit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setObjectName("actionQuit")
        self.menuHelp = QtWidgets.QMenu(parent=self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(parent=self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setText("Open...")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setText("Save")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setText("Save As...")
        self.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionHelp = QtGui.QAction(parent=MainWindow)
        self.actionHelp.setText("Help")
        self.actionHelp.setShortcut("Ctrl+?")
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setText("About")
        self.actionAbout.setShortcut("")
        self.actionAbout.setMenuRole(QtGui.QAction.MenuRole.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtGui.QAction(parent=MainWindow)
        self.actionAboutQt.setText("About Qt")
        self.actionAboutQt.setShortcut("")
        self.actionAboutQt.setMenuRole(QtGui.QAction.MenuRole.AboutQtRole)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setText("Settings")
        self.actionSettings.setShortcut("")
        self.actionSettings.setMenuRole(QtGui.QAction.MenuRole.PreferencesRole)
        self.actionSettings.setObjectName("actionSettings")
        self.actionCut = QtGui.QAction(parent=MainWindow)
        self.actionCut.setText("Cut")
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        self.actionCopy.setText("Copy")
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        self.actionPaste.setText("Paste")
        self.actionPaste.setShortcut("Ctrl+V")
        self.actionPaste.setObjectName("actionPaste")
        self.actionApply = QtGui.QAction(parent=MainWindow)
        self.actionApply.setText("Apply...")
        self.actionApply.setShortcut("")
        self.actionApply.setObjectName("actionApply")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionApply)
        self.menuFile.addAction(self.menuOpen_ApplyRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_Recent.setTitle(_translate("MainWindow", "Open Recent"))
        self.menuOpen_ApplyRecent.setTitle(_translate("MainWindow", "Apply Recent"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", " Edit"))
from uic.mplwidget import mplwidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
