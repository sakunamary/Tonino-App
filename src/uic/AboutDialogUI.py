# Form implementation generated from reading ui file 'ui/AboutDialogUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 226)
        Dialog.setWindowTitle("")
        Dialog.setModal(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoLabel = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setMinimumSize(QtCore.QSize(200, 200))
        self.logoLabel.setMaximumSize(QtCore.QSize(200, 200))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/app/icons/tonino_small.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")
        self.horizontalLayout.addWidget(self.logoLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.nameLabel = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setToolTip("")
        self.nameLabel.setAccessibleDescription("")
        self.nameLabel.setText("Tonino")
        self.nameLabel.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.debugLabel = QtWidgets.QLabel(parent=Dialog)
        self.debugLabel.setText("")
        self.debugLabel.setObjectName("debugLabel")
        self.verticalLayout.addWidget(self.debugLabel)
        self.versionLabel = QtWidgets.QLabel(parent=Dialog)
        self.versionLabel.setToolTip("")
        self.versionLabel.setAccessibleDescription("")
        self.versionLabel.setText("Version")
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        self.copyrightLabel = QtWidgets.QLabel(parent=Dialog)
        self.copyrightLabel.setToolTip("")
        self.copyrightLabel.setAccessibleDescription("")
        self.copyrightLabel.setText("Copyright © 2023 Marko Luther, Paul Holleis")
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.verticalLayout.addWidget(self.copyrightLabel)
        self.serialLabel = QtWidgets.QLabel(parent=Dialog)
        self.serialLabel.setToolTip("")
        self.serialLabel.setAccessibleDescription("")
        self.serialLabel.setText("Serial")
        self.serialLabel.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.serialLabel.setObjectName("serialLabel")
        self.verticalLayout.addWidget(self.serialLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalButtonLayout = QtWidgets.QHBoxLayout()
        self.horizontalButtonLayout.setObjectName("horizontalButtonLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalButtonLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setToolTip("")
        self.pushButton.setAccessibleDescription("")
        self.pushButton.setText("OK")
        self.pushButton.setObjectName("pushButton")
        self.horizontalButtonLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalButtonLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
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
