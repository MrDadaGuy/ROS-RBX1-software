# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ardec/PycharmProjects/RBX1/rbx1/ui/manualcommands.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 270, 171, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit_Roll = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_Roll.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.plainTextEdit_Roll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Roll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Roll.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Roll.setPlainText("0")
        self.plainTextEdit_Roll.setObjectName("plainTextEdit_Roll")
        self.verticalLayout_2.addWidget(self.plainTextEdit_Roll)
        self.plainTextEdit_Pitch = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_Pitch.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.plainTextEdit_Pitch.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Pitch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Pitch.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Pitch.setPlainText("0")
        self.plainTextEdit_Pitch.setObjectName("plainTextEdit_Pitch")
        self.verticalLayout_2.addWidget(self.plainTextEdit_Pitch)
        self.plainTextEdit_Yaw = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_Yaw.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.plainTextEdit_Yaw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Yaw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Yaw.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Yaw.setPlainText("0")
        self.plainTextEdit_Yaw.setObjectName("plainTextEdit_Yaw")
        self.verticalLayout_2.addWidget(self.plainTextEdit_Yaw)
        self.pushButtonShiftPosition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShiftPosition.setGeometry(QtCore.QRect(50, 200, 131, 27))
        self.pushButtonShiftPosition.setObjectName("pushButtonShiftPosition")
        self.pushButtonSetOrientation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetOrientation.setGeometry(QtCore.QRect(50, 410, 131, 27))
        self.pushButtonSetOrientation.setObjectName("pushButtonSetOrientation")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 241, 131))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Z_Minus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Z_Minus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_Z_Minus.setObjectName("pushButton_Z_Minus")
        self.gridLayout.addWidget(self.pushButton_Z_Minus, 2, 1, 1, 1)
        self.plainTextEdit_X = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_X.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.plainTextEdit_X.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_X.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_X.setObjectName("plainTextEdit_X")
        self.gridLayout.addWidget(self.plainTextEdit_X, 0, 0, 1, 1)
        self.pushButton_Y_Minus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Y_Minus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_Y_Minus.setObjectName("pushButton_Y_Minus")
        self.gridLayout.addWidget(self.pushButton_Y_Minus, 1, 1, 1, 1)
        self.plainTextEdit_Z = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Z.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.plainTextEdit_Z.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Z.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Z.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Z.setPlainText("0")
        self.plainTextEdit_Z.setObjectName("plainTextEdit_Z")
        self.gridLayout.addWidget(self.plainTextEdit_Z, 2, 0, 1, 1)
        self.pushButton_X_Minus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_X_Minus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_X_Minus.setObjectName("pushButton_X_Minus")
        self.gridLayout.addWidget(self.pushButton_X_Minus, 0, 1, 1, 1)
        self.plainTextEdit_Y = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Y.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.plainTextEdit_Y.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Y.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Y.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Y.setPlainText("0")
        self.plainTextEdit_Y.setObjectName("plainTextEdit_Y")
        self.gridLayout.addWidget(self.plainTextEdit_Y, 1, 0, 1, 1)
        self.pushButton_X_Plus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_X_Plus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_X_Plus.setObjectName("pushButton_X_Plus")
        self.gridLayout.addWidget(self.pushButton_X_Plus, 0, 2, 1, 1)
        self.pushButton_Y_Plus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Y_Plus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_Y_Plus.setObjectName("pushButton_Y_Plus")
        self.gridLayout.addWidget(self.pushButton_Y_Plus, 1, 2, 1, 1)
        self.pushButton_Z_Plus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Z_Plus.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_Z_Plus.setObjectName("pushButton_Z_Plus")
        self.gridLayout.addWidget(self.pushButton_Z_Plus, 2, 2, 1, 1)
        self.pushButtonRandomTarget = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRandomTarget.setGeometry(QtCore.QRect(170, 520, 131, 27))
        self.pushButtonRandomTarget.setObjectName("pushButtonRandomTarget")
        self.pushButtonSetPosition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetPosition.setGeometry(QtCore.QRect(50, 170, 131, 27))
        self.pushButtonSetPosition.setObjectName("pushButtonSetPosition")
        self.pushButtonSetPoseTarget = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetPoseTarget.setGeometry(QtCore.QRect(170, 490, 131, 27))
        self.pushButtonSetPoseTarget.setObjectName("pushButtonSetPoseTarget")
        self.pushButtonShiftOrientation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShiftOrientation.setGeometry(QtCore.QRect(50, 440, 131, 27))
        self.pushButtonShiftOrientation.setObjectName("pushButtonShiftOrientation")
        self.pushButtonRefreshStatus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRefreshStatus.setGeometry(QtCore.QRect(50, 520, 111, 27))
        self.pushButtonRefreshStatus.setObjectName("pushButtonRefreshStatus")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 20, 311, 238))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSliderJoint_3 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_3.setObjectName("horizontalSliderJoint_3")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalSliderJoint_2 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_2.setObjectName("horizontalSliderJoint_2")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_2, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.horizontalSliderJoint_4 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_4.setObjectName("horizontalSliderJoint_4")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalSliderJoint_1 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_1.setObjectName("horizontalSliderJoint_1")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_1, 5, 1, 1, 1)
        self.pushButtonSetJointTarget = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonSetJointTarget.setObjectName("pushButtonSetJointTarget")
        self.gridLayout_2.addWidget(self.pushButtonSetJointTarget, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalSliderJoint_5 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_5.setMinimum(-100)
        self.horizontalSliderJoint_5.setMaximum(100)
        self.horizontalSliderJoint_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_5.setObjectName("horizontalSliderJoint_5")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_5, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.labelJoint5 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint5.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint5.setObjectName("labelJoint5")
        self.gridLayout_2.addWidget(self.labelJoint5, 1, 2, 1, 1)
        self.labelJoint4 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint4.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint4.setObjectName("labelJoint4")
        self.gridLayout_2.addWidget(self.labelJoint4, 2, 2, 1, 1)
        self.labelJoint2 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint2.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint2.setObjectName("labelJoint2")
        self.gridLayout_2.addWidget(self.labelJoint2, 4, 2, 1, 1)
        self.labelJoint3 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint3.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint3.setObjectName("labelJoint3")
        self.gridLayout_2.addWidget(self.labelJoint3, 3, 2, 1, 1)
        self.labelJoint1 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint1.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint1.setObjectName("labelJoint1")
        self.gridLayout_2.addWidget(self.labelJoint1, 5, 2, 1, 1)
        self.horizontalSliderJoint_6 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_6.setObjectName("horizontalSliderJoint_6")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_6, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.labelJoint6 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint6.setObjectName("labelJoint6")
        self.gridLayout_2.addWidget(self.labelJoint6, 0, 2, 1, 1)
        self.pushButtonOpenGripper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpenGripper.setGeometry(QtCore.QRect(578, 290, 111, 27))
        self.pushButtonOpenGripper.setObjectName("pushButtonOpenGripper")
        self.pushButtonCloseGripper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCloseGripper.setGeometry(QtCore.QRect(578, 330, 111, 27))
        self.pushButtonCloseGripper.setObjectName("pushButtonCloseGripper")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSliderJoint_5.valueChanged['int'].connect(self.labelJoint5.setNum)
        self.horizontalSliderJoint_4.valueChanged['int'].connect(self.labelJoint4.setNum)
        self.horizontalSliderJoint_3.valueChanged['int'].connect(self.labelJoint3.setNum)
        self.horizontalSliderJoint_2.valueChanged['int'].connect(self.labelJoint2.setNum)
        self.horizontalSliderJoint_1.valueChanged['int'].connect(self.labelJoint1.setNum)
        self.horizontalSliderJoint_6.valueChanged['int'].connect(self.labelJoint6.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Roll / Pitch / Yaw Target"))
        self.pushButtonShiftPosition.setText(_translate("MainWindow", "Shift Position"))
        self.pushButtonSetOrientation.setText(_translate("MainWindow", "Set Orientation"))
        self.groupBox.setTitle(_translate("MainWindow", "X Y Z Target"))
        self.pushButton_Z_Minus.setText(_translate("MainWindow", "-"))
        self.plainTextEdit_X.setPlainText(_translate("MainWindow", "0"))
        self.pushButton_Y_Minus.setText(_translate("MainWindow", "-"))
        self.pushButton_X_Minus.setText(_translate("MainWindow", "-"))
        self.pushButton_X_Plus.setText(_translate("MainWindow", "+"))
        self.pushButton_Y_Plus.setText(_translate("MainWindow", "+"))
        self.pushButton_Z_Plus.setText(_translate("MainWindow", "+"))
        self.pushButtonRandomTarget.setText(_translate("MainWindow", "Random Target"))
        self.pushButtonSetPosition.setText(_translate("MainWindow", "Set Position"))
        self.pushButtonSetPoseTarget.setText(_translate("MainWindow", "Set Pose Target"))
        self.pushButtonShiftOrientation.setText(_translate("MainWindow", "Shift Orientation"))
        self.pushButtonRefreshStatus.setText(_translate("MainWindow", "Refresh Status"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Joints Target (Degrees)"))
        self.label_4.setText(_translate("MainWindow", "Joint 2"))
        self.label_5.setText(_translate("MainWindow", "Joint 1"))
        self.label_3.setText(_translate("MainWindow", "Joint 3"))
        self.pushButtonSetJointTarget.setText(_translate("MainWindow", "Set Joint Target"))
        self.label.setText(_translate("MainWindow", "Joint 5"))
        self.label_2.setText(_translate("MainWindow", "Joint 4"))
        self.labelJoint5.setText(_translate("MainWindow", "0"))
        self.labelJoint4.setText(_translate("MainWindow", "0"))
        self.labelJoint2.setText(_translate("MainWindow", "0"))
        self.labelJoint3.setText(_translate("MainWindow", "0"))
        self.labelJoint1.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Joint 6"))
        self.labelJoint6.setText(_translate("MainWindow", "0"))
        self.pushButtonOpenGripper.setText(_translate("MainWindow", "Open Gripper"))
        self.pushButtonCloseGripper.setText(_translate("MainWindow", "Close Gripper"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

