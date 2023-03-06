# Form implementation generated from reading ui file 'ui/PreCalibDialogUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(575, 389)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setWindowTitle("PreCalibration")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logOutput = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.logOutput.setToolTip("")
        self.logOutput.setAccessibleDescription("")
        self.logOutput.setObjectName("logOutput")
        self.horizontalLayout_2.addWidget(self.logOutput)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonClear = QtWidgets.QPushButton(parent=Dialog)
        self.pushButtonClear.setToolTip("")
        self.pushButtonClear.setAccessibleDescription("")
        self.pushButtonClear.setText("Clear")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.verticalLayout_3.addWidget(self.pushButtonClear)
        self.pushButtonMaster = QtWidgets.QPushButton(parent=Dialog)
        self.pushButtonMaster.setToolTip("")
        self.pushButtonMaster.setAccessibleDescription("")
        self.pushButtonMaster.setText("Master")
        self.pushButtonMaster.setObjectName("pushButtonMaster")
        self.verticalLayout_3.addWidget(self.pushButtonMaster)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButtonScan = QtWidgets.QPushButton(parent=Dialog)
        self.pushButtonScan.setToolTip("")
        self.pushButtonScan.setAccessibleDescription("")
        self.pushButtonScan.setText("Scan")
        self.pushButtonScan.setObjectName("pushButtonScan")
        self.verticalLayout_3.addWidget(self.pushButtonScan)
        self.pushButtonPreCal = QtWidgets.QPushButton(parent=Dialog)
        self.pushButtonPreCal.setToolTip("")
        self.pushButtonPreCal.setAccessibleDescription("")
        self.pushButtonPreCal.setText("PreCal")
        self.pushButtonPreCal.setObjectName("pushButtonPreCal")
        self.verticalLayout_3.addWidget(self.pushButtonPreCal)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButtonSet = QtWidgets.QPushButton(parent=Dialog)
        self.pushButtonSet.setToolTip("")
        self.pushButtonSet.setAccessibleDescription("")
        self.pushButtonSet.setText("Set")
        self.pushButtonSet.setObjectName("pushButtonSet")
        self.verticalLayout_3.addWidget(self.pushButtonSet)
        self.pushButtonReset = QtWidgets.QPushButton(parent=Dialog)
        self.pushButtonReset.setToolTip("")
        self.pushButtonReset.setAccessibleDescription("")
        self.pushButtonReset.setText("Reset")
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.verticalLayout_3.addWidget(self.pushButtonReset)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setToolTip("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
