# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historyparser.ui'
#
# Created: Sat May 10 17:22:56 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HandHistoryParserDlg(object):
    def setupUi(self, HandHistoryParserDlg):
        HandHistoryParserDlg.setObjectName(_fromUtf8("HandHistoryParserDlg"))
        HandHistoryParserDlg.resize(362, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/transfer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HandHistoryParserDlg.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(HandHistoryParserDlg)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(HandHistoryParserDlg)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEditHistory = QtGui.QTextEdit(self.groupBox)
        self.textEditHistory.setObjectName(_fromUtf8("textEditHistory"))
        self.verticalLayout.addWidget(self.textEditHistory)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditInputFile = QtGui.QLineEdit(self.groupBox)
        self.lineEditInputFile.setReadOnly(True)
        self.lineEditInputFile.setObjectName(_fromUtf8("lineEditInputFile"))
        self.horizontalLayout_2.addWidget(self.lineEditInputFile)
        self.buttonInputFile = QtGui.QPushButton(self.groupBox)
        self.buttonInputFile.setObjectName(_fromUtf8("buttonInputFile"))
        self.horizontalLayout_2.addWidget(self.buttonInputFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditInputFolder = QtGui.QLineEdit(self.groupBox)
        self.lineEditInputFolder.setReadOnly(True)
        self.lineEditInputFolder.setObjectName(_fromUtf8("lineEditInputFolder"))
        self.horizontalLayout.addWidget(self.lineEditInputFolder)
        self.buttonInputFolder = QtGui.QPushButton(self.groupBox)
        self.buttonInputFolder.setObjectName(_fromUtf8("buttonInputFolder"))
        self.horizontalLayout.addWidget(self.buttonInputFolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(HandHistoryParserDlg)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditOutputFile = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditOutputFile.setReadOnly(True)
        self.lineEditOutputFile.setObjectName(_fromUtf8("lineEditOutputFile"))
        self.horizontalLayout_3.addWidget(self.lineEditOutputFile)
        self.buttonOutputFile = QtGui.QPushButton(self.groupBox_2)
        self.buttonOutputFile.setObjectName(_fromUtf8("buttonOutputFile"))
        self.horizontalLayout_3.addWidget(self.buttonOutputFile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditOutputFolder = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditOutputFolder.setReadOnly(True)
        self.lineEditOutputFolder.setObjectName(_fromUtf8("lineEditOutputFolder"))
        self.horizontalLayout_4.addWidget(self.lineEditOutputFolder)
        self.buttonOutputFolder = QtGui.QPushButton(self.groupBox_2)
        self.buttonOutputFolder.setObjectName(_fromUtf8("buttonOutputFolder"))
        self.horizontalLayout_4.addWidget(self.buttonOutputFolder)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 10, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.buttonParse = QtGui.QPushButton(HandHistoryParserDlg)
        self.buttonParse.setObjectName(_fromUtf8("buttonParse"))
        self.horizontalLayout_5.addWidget(self.buttonParse)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(HandHistoryParserDlg)
        QtCore.QMetaObject.connectSlotsByName(HandHistoryParserDlg)

    def retranslateUi(self, HandHistoryParserDlg):
        HandHistoryParserDlg.setWindowTitle(_translate("HandHistoryParserDlg", "HandHistoryParser", None))
        self.groupBox.setTitle(_translate("HandHistoryParserDlg", "Input", None))
        self.label.setText(_translate("HandHistoryParserDlg", "Input Text", None))
        self.label_2.setText(_translate("HandHistoryParserDlg", "Input File", None))
        self.buttonInputFile.setText(_translate("HandHistoryParserDlg", "Select File", None))
        self.label_3.setText(_translate("HandHistoryParserDlg", "Input Folder", None))
        self.buttonInputFolder.setText(_translate("HandHistoryParserDlg", "Select Folder", None))
        self.groupBox_2.setTitle(_translate("HandHistoryParserDlg", "Output", None))
        self.label_4.setText(_translate("HandHistoryParserDlg", "Output File", None))
        self.buttonOutputFile.setText(_translate("HandHistoryParserDlg", "Select File", None))
        self.label_5.setText(_translate("HandHistoryParserDlg", "Output Folder", None))
        self.buttonOutputFolder.setText(_translate("HandHistoryParserDlg", "Select Folder", None))
        self.buttonParse.setText(_translate("HandHistoryParserDlg", "Parse", None))
