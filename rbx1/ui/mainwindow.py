# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ardec/PycharmProjects/RBX1/rbx1/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 662)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonSCK_MOD = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonSCK_MOD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSCK_MOD.sizePolicy().hasHeightForWidth())
        self.pushButtonSCK_MOD.setSizePolicy(sizePolicy)
        self.pushButtonSCK_MOD.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonSCK_MOD.setStyleSheet("")
        self.pushButtonSCK_MOD.setObjectName("pushButtonSCK_MOD")
        self.gridLayout_3.addWidget(self.pushButtonSCK_MOD, 1, 0, 1, 1)
        self.pushButtonTH_SD = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonTH_SD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTH_SD.sizePolicy().hasHeightForWidth())
        self.pushButtonTH_SD.setSizePolicy(sizePolicy)
        self.pushButtonTH_SD.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonTH_SD.setObjectName("pushButtonTH_SD")
        self.gridLayout_3.addWidget(self.pushButtonTH_SD, 1, 4, 1, 1)
        self.pushButtonTH_WRN = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonTH_WRN.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTH_WRN.sizePolicy().hasHeightForWidth())
        self.pushButtonTH_WRN.setSizePolicy(sizePolicy)
        self.pushButtonTH_WRN.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonTH_WRN.setObjectName("pushButtonTH_WRN")
        self.gridLayout_3.addWidget(self.pushButtonTH_WRN, 1, 5, 1, 1)
        self.pushButtonNOTPERF_CMD = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonNOTPERF_CMD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonNOTPERF_CMD.sizePolicy().hasHeightForWidth())
        self.pushButtonNOTPERF_CMD.setSizePolicy(sizePolicy)
        self.pushButtonNOTPERF_CMD.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonNOTPERF_CMD.setObjectName("pushButtonNOTPERF_CMD")
        self.gridLayout_3.addWidget(self.pushButtonNOTPERF_CMD, 2, 0, 1, 1)
        self.pushButtonSTEP_LOSS_B = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonSTEP_LOSS_B.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSTEP_LOSS_B.sizePolicy().hasHeightForWidth())
        self.pushButtonSTEP_LOSS_B.setSizePolicy(sizePolicy)
        self.pushButtonSTEP_LOSS_B.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonSTEP_LOSS_B.setObjectName("pushButtonSTEP_LOSS_B")
        self.gridLayout_3.addWidget(self.pushButtonSTEP_LOSS_B, 1, 1, 1, 1)
        self.pushButtonOCD = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonOCD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOCD.sizePolicy().hasHeightForWidth())
        self.pushButtonOCD.setSizePolicy(sizePolicy)
        self.pushButtonOCD.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonOCD.setObjectName("pushButtonOCD")
        self.gridLayout_3.addWidget(self.pushButtonOCD, 1, 3, 1, 1)
        self.pushButtonSTEP_LOSS_A = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonSTEP_LOSS_A.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSTEP_LOSS_A.sizePolicy().hasHeightForWidth())
        self.pushButtonSTEP_LOSS_A.setSizePolicy(sizePolicy)
        self.pushButtonSTEP_LOSS_A.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonSTEP_LOSS_A.setObjectName("pushButtonSTEP_LOSS_A")
        self.gridLayout_3.addWidget(self.pushButtonSTEP_LOSS_A, 1, 2, 1, 1)
        self.pushButtonWRONG_CMD = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonWRONG_CMD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonWRONG_CMD.sizePolicy().hasHeightForWidth())
        self.pushButtonWRONG_CMD.setSizePolicy(sizePolicy)
        self.pushButtonWRONG_CMD.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonWRONG_CMD.setObjectName("pushButtonWRONG_CMD")
        self.gridLayout_3.addWidget(self.pushButtonWRONG_CMD, 1, 7, 1, 1)
        self.pushButtonDIR = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonDIR.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDIR.sizePolicy().hasHeightForWidth())
        self.pushButtonDIR.setSizePolicy(sizePolicy)
        self.pushButtonDIR.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonDIR.setObjectName("pushButtonDIR")
        self.gridLayout_3.addWidget(self.pushButtonDIR, 2, 3, 1, 1)
        self.pushButtonSW_EVN = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonSW_EVN.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSW_EVN.sizePolicy().hasHeightForWidth())
        self.pushButtonSW_EVN.setSizePolicy(sizePolicy)
        self.pushButtonSW_EVN.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonSW_EVN.setObjectName("pushButtonSW_EVN")
        self.gridLayout_3.addWidget(self.pushButtonSW_EVN, 2, 4, 1, 1)
        self.pushButtonSW_F = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonSW_F.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSW_F.sizePolicy().hasHeightForWidth())
        self.pushButtonSW_F.setSizePolicy(sizePolicy)
        self.pushButtonSW_F.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonSW_F.setObjectName("pushButtonSW_F")
        self.gridLayout_3.addWidget(self.pushButtonSW_F, 2, 5, 1, 1)
        self.pushButtonBusy = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonBusy.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBusy.sizePolicy().hasHeightForWidth())
        self.pushButtonBusy.setSizePolicy(sizePolicy)
        self.pushButtonBusy.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonBusy.setStyleSheet("")
        self.pushButtonBusy.setObjectName("pushButtonBusy")
        self.gridLayout_3.addWidget(self.pushButtonBusy, 2, 6, 1, 1)
        self.pushButtonHiZ = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonHiZ.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHiZ.sizePolicy().hasHeightForWidth())
        self.pushButtonHiZ.setSizePolicy(sizePolicy)
        self.pushButtonHiZ.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonHiZ.setStyleSheet("")
        self.pushButtonHiZ.setObjectName("pushButtonHiZ")
        self.gridLayout_3.addWidget(self.pushButtonHiZ, 2, 7, 1, 1)
        self.pushButtonUVLO = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonUVLO.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonUVLO.sizePolicy().hasHeightForWidth())
        self.pushButtonUVLO.setSizePolicy(sizePolicy)
        self.pushButtonUVLO.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonUVLO.setObjectName("pushButtonUVLO")
        self.gridLayout_3.addWidget(self.pushButtonUVLO, 1, 6, 1, 1)
        self.pushButtonMOT_STATUS = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonMOT_STATUS.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMOT_STATUS.sizePolicy().hasHeightForWidth())
        self.pushButtonMOT_STATUS.setSizePolicy(sizePolicy)
        self.pushButtonMOT_STATUS.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonMOT_STATUS.setStyleSheet("")
        self.pushButtonMOT_STATUS.setObjectName("pushButtonMOT_STATUS")
        self.gridLayout_3.addWidget(self.pushButtonMOT_STATUS, 2, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox_4, 4, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(50, 100))
        self.groupBox.setObjectName("groupBox")
        self.pushFree = QtWidgets.QPushButton(self.groupBox)
        self.pushFree.setGeometry(QtCore.QRect(310, 80, 99, 27))
        self.pushFree.setObjectName("pushFree")
        self.pushEasyRun = QtWidgets.QPushButton(self.groupBox)
        self.pushEasyRun.setGeometry(QtCore.QRect(310, 40, 99, 27))
        self.pushEasyRun.setObjectName("pushEasyRun")
        self.frameMotor = QtWidgets.QFrame(self.groupBox)
        self.frameMotor.setGeometry(QtCore.QRect(10, 30, 291, 311))
        self.frameMotor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMotor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMotor.setObjectName("frameMotor")
        self.formLayout = QtWidgets.QFormLayout(self.frameMotor)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frameMotor)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.plainTextEditPosition = QtWidgets.QPlainTextEdit(self.frameMotor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditPosition.sizePolicy().hasHeightForWidth())
        self.plainTextEditPosition.setSizePolicy(sizePolicy)
        self.plainTextEditPosition.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEditPosition.setReadOnly(True)
        self.plainTextEditPosition.setObjectName("plainTextEditPosition")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEditPosition)
        self.label_2 = QtWidgets.QLabel(self.frameMotor)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.plainTextEditSpeed = QtWidgets.QPlainTextEdit(self.frameMotor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditSpeed.sizePolicy().hasHeightForWidth())
        self.plainTextEditSpeed.setSizePolicy(sizePolicy)
        self.plainTextEditSpeed.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEditSpeed.setReadOnly(True)
        self.plainTextEditSpeed.setObjectName("plainTextEditSpeed")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEditSpeed)
        self.label_3 = QtWidgets.QLabel(self.frameMotor)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEditTarget = QtWidgets.QTextEdit(self.frameMotor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditTarget.sizePolicy().hasHeightForWidth())
        self.textEditTarget.setSizePolicy(sizePolicy)
        self.textEditTarget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEditTarget.setReadOnly(True)
        self.textEditTarget.setObjectName("textEditTarget")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEditTarget)
        self.plainTextEditStatus = QtWidgets.QPlainTextEdit(self.frameMotor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditStatus.sizePolicy().hasHeightForWidth())
        self.plainTextEditStatus.setSizePolicy(sizePolicy)
        self.plainTextEditStatus.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEditStatus.setObjectName("plainTextEditStatus")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plainTextEditStatus)
        self.label_4 = QtWidgets.QLabel(self.frameMotor)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.listMotors = QtWidgets.QListWidget(self.frameMotor)
        self.listMotors.setObjectName("listMotors")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.listMotors)
        self.pushHardStop = QtWidgets.QPushButton(self.groupBox)
        self.pushHardStop.setGeometry(QtCore.QRect(310, 120, 99, 27))
        self.pushHardStop.setObjectName("pushHardStop")
        self.pushSoftStop = QtWidgets.QPushButton(self.groupBox)
        self.pushSoftStop.setGeometry(QtCore.QRect(310, 160, 99, 27))
        self.pushSoftStop.setObjectName("pushSoftStop")
        self.pushButton_HIZ = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_HIZ.setGeometry(QtCore.QRect(310, 200, 99, 27))
        self.pushButton_HIZ.setObjectName("pushButton_HIZ")
        self.pushButton_ResetStatus = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ResetStatus.setGeometry(QtCore.QRect(310, 240, 99, 27))
        self.pushButton_ResetStatus.setObjectName("pushButton_ResetStatus")
        self.pushButtonCloseGripper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonCloseGripper.setGeometry(QtCore.QRect(310, 370, 99, 27))
        self.pushButtonCloseGripper.setObjectName("pushButtonCloseGripper")
        self.pushButtonOpenGripper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonOpenGripper.setGeometry(QtCore.QRect(200, 370, 99, 27))
        self.pushButtonOpenGripper.setObjectName("pushButtonOpenGripper")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 50, 311, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSliderJoint_4 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_4.setObjectName("horizontalSliderJoint_4")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.horizontalSliderJoint_5 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_5.setMinimum(0)
        self.horizontalSliderJoint_5.setMaximum(99)
        self.horizontalSliderJoint_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_5.setObjectName("horizontalSliderJoint_5")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_5, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.labelJoint5 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint5.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint5.setObjectName("labelJoint5")
        self.gridLayout_2.addWidget(self.labelJoint5, 1, 2, 1, 1)
        self.horizontalSliderJoint_2 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_2.setObjectName("horizontalSliderJoint_2")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_2, 4, 1, 1, 1)
        self.horizontalSliderJoint_3 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_3.setObjectName("horizontalSliderJoint_3")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_3, 3, 1, 1, 1)
        self.labelJoint4 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint4.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint4.setObjectName("labelJoint4")
        self.gridLayout_2.addWidget(self.labelJoint4, 2, 2, 1, 1)
        self.labelJoint1 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint1.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint1.setObjectName("labelJoint1")
        self.gridLayout_2.addWidget(self.labelJoint1, 5, 2, 1, 1)
        self.labelJoint2 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint2.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint2.setObjectName("labelJoint2")
        self.gridLayout_2.addWidget(self.labelJoint2, 4, 2, 1, 1)
        self.labelJoint3 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint3.setMinimumSize(QtCore.QSize(30, 0))
        self.labelJoint3.setObjectName("labelJoint3")
        self.gridLayout_2.addWidget(self.labelJoint3, 3, 2, 1, 1)
        self.pushButtonHIZAll = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonHIZAll.setObjectName("pushButtonHIZAll")
        self.gridLayout_2.addWidget(self.pushButtonHIZAll, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.horizontalSliderJoint_6 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_6.setObjectName("horizontalSliderJoint_6")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_6, 0, 1, 1, 1)
        self.labelJoint6 = QtWidgets.QLabel(self.groupBox_3)
        self.labelJoint6.setObjectName("labelJoint6")
        self.gridLayout_2.addWidget(self.labelJoint6, 0, 2, 1, 1)
        self.horizontalSliderJoint_1 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderJoint_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderJoint_1.setObjectName("horizontalSliderJoint_1")
        self.gridLayout_2.addWidget(self.horizontalSliderJoint_1, 5, 1, 1, 1)
        self.pushButtonMove = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonMove.setObjectName("pushButtonMove")
        self.gridLayout_2.addWidget(self.pushButtonMove, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushFreeAll = QtWidgets.QPushButton(self.groupBox_3)
        self.pushFreeAll.setObjectName("pushFreeAll")
        self.gridLayout_2.addWidget(self.pushFreeAll, 7, 0, 1, 1)
        self.pushButtonGoHome = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonGoHome.setObjectName("pushButtonGoHome")
        self.gridLayout_2.addWidget(self.pushButtonGoHome, 7, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 926, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuRBX1_Control_Station = QtWidgets.QMenu(self.menuBar)
        self.menuRBX1_Control_Station.setObjectName("menuRBX1_Control_Station")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuRBX1_Control_Station.addAction(self.actionExit)
        self.menuBar.addAction(self.menuRBX1_Control_Station.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSliderJoint_6.valueChanged['int'].connect(self.labelJoint6.setNum)
        self.horizontalSliderJoint_5.valueChanged['int'].connect(self.labelJoint5.setNum)
        self.horizontalSliderJoint_4.valueChanged['int'].connect(self.labelJoint4.setNum)
        self.horizontalSliderJoint_3.valueChanged['int'].connect(self.labelJoint3.setNum)
        self.horizontalSliderJoint_2.valueChanged['int'].connect(self.labelJoint2.setNum)
        self.horizontalSliderJoint_1.valueChanged['int'].connect(self.labelJoint1.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Status"))
        self.pushButtonSCK_MOD.setText(_translate("MainWindow", "SCK_MOD"))
        self.pushButtonTH_SD.setText(_translate("MainWindow", "TH_SD"))
        self.pushButtonTH_WRN.setText(_translate("MainWindow", "TH_WRN"))
        self.pushButtonNOTPERF_CMD.setText(_translate("MainWindow", "NOTPERF_CMD"))
        self.pushButtonSTEP_LOSS_B.setText(_translate("MainWindow", "STEP_LOSS_B"))
        self.pushButtonOCD.setText(_translate("MainWindow", "OCD"))
        self.pushButtonSTEP_LOSS_A.setText(_translate("MainWindow", "STEP_LOSS_A"))
        self.pushButtonWRONG_CMD.setText(_translate("MainWindow", "WRONG_CMD"))
        self.pushButtonDIR.setText(_translate("MainWindow", "DIR"))
        self.pushButtonSW_EVN.setText(_translate("MainWindow", "SW_EVN"))
        self.pushButtonSW_F.setText(_translate("MainWindow", "SW_F"))
        self.pushButtonBusy.setText(_translate("MainWindow", "Busy"))
        self.pushButtonHiZ.setText(_translate("MainWindow", "HiZ"))
        self.pushButtonUVLO.setText(_translate("MainWindow", "UVLO"))
        self.pushButtonMOT_STATUS.setText(_translate("MainWindow", "MOT_STATUS"))
        self.groupBox.setTitle(_translate("MainWindow", "Motor Status"))
        self.pushFree.setText(_translate("MainWindow", "Free"))
        self.pushEasyRun.setText(_translate("MainWindow", "Easy Run"))
        self.frameMotor.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Position"))
        self.label_2.setText(_translate("MainWindow", "Speed"))
        self.label_3.setText(_translate("MainWindow", "Target"))
        self.textEditTarget.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Status"))
        self.pushHardStop.setText(_translate("MainWindow", "Hard Stop"))
        self.pushSoftStop.setText(_translate("MainWindow", "Soft Stop"))
        self.pushButton_HIZ.setText(_translate("MainWindow", "HiZ"))
        self.pushButton_ResetStatus.setText(_translate("MainWindow", "Reset Status"))
        self.pushButtonCloseGripper.setText(_translate("MainWindow", "Close Gripper"))
        self.pushButtonOpenGripper.setText(_translate("MainWindow", "Open Gripper"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Motor Control"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Joints Target (Degrees)"))
        self.label_7.setText(_translate("MainWindow", "Shoulder"))
        self.label_9.setText(_translate("MainWindow", "Elbow"))
        self.labelJoint5.setText(_translate("MainWindow", "0"))
        self.labelJoint4.setText(_translate("MainWindow", "0"))
        self.labelJoint1.setText(_translate("MainWindow", "0"))
        self.labelJoint2.setText(_translate("MainWindow", "0"))
        self.labelJoint3.setText(_translate("MainWindow", "0"))
        self.pushButtonHIZAll.setText(_translate("MainWindow", "HIZ All"))
        self.label_10.setText(_translate("MainWindow", "Wrist Rot"))
        self.labelJoint6.setText(_translate("MainWindow", "0"))
        self.pushButtonMove.setText(_translate("MainWindow", "Move"))
        self.label_8.setText(_translate("MainWindow", "Wrist"))
        self.label_6.setText(_translate("MainWindow", "Base Rot"))
        self.label_5.setText(_translate("MainWindow", "Dual Base"))
        self.pushFreeAll.setText(_translate("MainWindow", "Free All"))
        self.pushButtonGoHome.setText(_translate("MainWindow", "Go Home"))
        self.menuRBX1_Control_Station.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

