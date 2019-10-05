# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Launcher.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

delay = 1000
hidden_mode = False
start_times = 3

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time as t
import subprocess

class Ui_BubbleBoiLauncher(object):
    def setupUi(self, BubbleBoiLauncher):
        BubbleBoiLauncher.setObjectName("BubbleBoiLauncher")
        BubbleBoiLauncher.resize(500, 500)
        BubbleBoiLauncher.setMinimumSize(QtCore.QSize(500, 500))
        BubbleBoiLauncher.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(BubbleBoiLauncher)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(119, 0, 262, 111))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.delay_label = QtWidgets.QLabel(self.centralwidget)
        self.delay_label.setGeometry(QtCore.QRect(10, 90, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.delay_label.setFont(font)
        self.delay_label.setObjectName("delay_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(34, 300, 430, 131))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.hidden_mode_label = QtWidgets.QLabel(self.centralwidget)
        self.hidden_mode_label.setGeometry(QtCore.QRect(10, 140, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hidden_mode_label.setFont(font)
        self.hidden_mode_label.setObjectName("hidden_mode_label")
        self.hidden_mode_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.hidden_mode_checkbox.setGeometry(QtCore.QRect(400, 168, 81, 20))
        self.hidden_mode_checkbox.setText("")
        self.hidden_mode_checkbox.setObjectName("hidden_mode_checkbox")
        self.start_times_label = QtWidgets.QLabel(self.centralwidget)
        self.start_times_label.setGeometry(QtCore.QRect(10, 190, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.start_times_label.setFont(font)
        self.start_times_label.setObjectName("start_times_label")
        self.one_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.one_start_radio.setGeometry(QtCore.QRect(140, 218, 31, 20))
        self.one_start_radio.setObjectName("one_start_radio")
        self.two_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.two_start_radio.setGeometry(QtCore.QRect(180, 218, 31, 20))
        self.two_start_radio.setObjectName("two_start_radio")
        self.three_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.three_start_radio.setGeometry(QtCore.QRect(220, 218, 31, 20))
        self.three_start_radio.setObjectName("three_start_radio")
        self.four_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.four_start_radio.setGeometry(QtCore.QRect(260, 218, 31, 20))
        self.four_start_radio.setObjectName("four_start_radio")
        self.five_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.five_start_radio.setGeometry(QtCore.QRect(300, 218, 31, 20))
        self.five_start_radio.setObjectName("five_start_radio")
        self.six_start_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.six_start_radio.setGeometry(QtCore.QRect(340, 218, 31, 20))
        self.six_start_radio.setObjectName("six_start_radio")
        self.delay_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.delay_comboBox.setGeometry(QtCore.QRect(230, 116, 73, 22))
        self.delay_comboBox.setObjectName("delay_comboBox")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        self.delay_comboBox.addItem("")
        BubbleBoiLauncher.setCentralWidget(self.centralwidget)
        self.start_button.clicked.connect(self.launched)

        self.retranslateUi(BubbleBoiLauncher)
        QtCore.QMetaObject.connectSlotsByName(BubbleBoiLauncher)

    def retranslateUi(self, BubbleBoiLauncher):
        _translate = QtCore.QCoreApplication.translate
        BubbleBoiLauncher.setWindowTitle(_translate("BubbleBoiLauncher", "BubbleBoiBot v1.73 - Launcher"))
        self.title_label.setText(_translate("BubbleBoiLauncher", "BubbleBoiBot v1.73"))
        self.delay_label.setText(_translate("BubbleBoiLauncher", "Delay (milliseconds):"))
        self.start_button.setText(_translate("BubbleBoiLauncher", "Launch"))
        self.hidden_mode_label.setText(_translate("BubbleBoiLauncher", "Hidden (Hide tasks in Task Manager):"))
        self.start_times_label.setText(_translate("BubbleBoiLauncher", "Start Times:"))
        self.one_start_radio.setText(_translate("BubbleBoiLauncher", "1"))
        self.two_start_radio.setText(_translate("BubbleBoiLauncher", "2"))
        self.three_start_radio.setText(_translate("BubbleBoiLauncher", "3"))
        self.four_start_radio.setText(_translate("BubbleBoiLauncher", "4"))
        self.five_start_radio.setText(_translate("BubbleBoiLauncher", "5"))
        self.six_start_radio.setText(_translate("BubbleBoiLauncher", "6"))
        self.delay_comboBox.setItemText(0, _translate("BubbleBoiLauncher", "250"))
        self.delay_comboBox.setItemText(1, _translate("BubbleBoiLauncher", "500"))
        self.delay_comboBox.setItemText(2, _translate("BubbleBoiLauncher", "750"))
        self.delay_comboBox.setItemText(3, _translate("BubbleBoiLauncher", "1000"))
        self.delay_comboBox.setItemText(4, _translate("BubbleBoiLauncher", "1250"))
        self.delay_comboBox.setItemText(5, _translate("BubbleBoiLauncher", "1500"))
        self.delay_comboBox.setItemText(6, _translate("BubbleBoiLauncher", "1750"))
        self.delay_comboBox.setItemText(7, _translate("BubbleBoiLauncher", "2000"))

    def launched(self):
    	global delay
    	global hidden_mode
    	global start_times
    	delay = int(self.delay_comboBox.currentText())

    	if self.hidden_mode_checkbox.isChecked():
    		hidden_mode = True
    	else:
    		hidden_mode = False

    	if self.one_start_radio.isChecked():
    		start_times = 1
    	elif self.two_start_radio.isChecked():
    		start_times = 2
    	elif self.three_start_radio.isChecked():
    		start_times = 3
    	elif self.four_start_radio.isChecked():
    		start_times = 4
    	elif self.five_start_radio.isChecked():
    		start_times = 5
    	elif self.six_start_radio.isChecked():
    		start_times = 6
    	elif not self.one_start_radio.isChecked() and not self.two_start_radio.isChecked() and not self.three_start_radio.isChecked() and not self.four_start_radio.isChecked() and not self.five_start_radio.isChecked() and not self.six_start_radio.isChecked():    		
    		start_times = "x"

    	if start_times != "x":
    		BubbleBoiLauncher.close()

    		if not hidden_mode:
    			for x in range(0, start_times):
    				    SW_MINIMIZE = 6
    				    info = subprocess.STARTUPINFO()
    				    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    				    info.wShowWindow = SW_MINIMIZE
    				    subprocess.Popen(r'loop5001.bat', startupinfo=info)
    				    t.sleep((delay/1000))

    			for x in range(0, start_times):
    				    SW_MINIMIZE = 6
    				    info = subprocess.STARTUPINFO()
    				    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    				    info.wShowWindow = SW_MINIMIZE
    				    subprocess.Popen(r'loop5002.bat', startupinfo=info)
    				    t.sleep((delay/1000))

    			for x in range(0, start_times):
    				    SW_MINIMIZE = 6
    				    info = subprocess.STARTUPINFO()
    				    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    				    info.wShowWindow = SW_MINIMIZE
    				    subprocess.Popen(r'loop5003.bat', startupinfo=info)
    				    t.sleep((delay/1000))
    		else:
    			for x in range(0, start_times):
    				    SW_HIDE = 0
    				    info = subprocess.STARTUPINFO()
    				    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    				    info.wShowWindow = SW_HIDE
    				    subprocess.Popen(r'loop5001.bat', startupinfo=info)
    				    t.sleep((delay/1000))

    			for x in range(0, start_times):
    				    SW_HIDE = 0
    				    info = subprocess.STARTUPINFO()
    				    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    				    info.wShowWindow = SW_HIDE
    				    subprocess.Popen(r'loop5002.bat', startupinfo=info)
    				    t.sleep((delay/1000))

    			for x in range(0, start_times):
    				    SW_HIDE = 0
    				    info = subprocess.STARTUPINFO()
    				    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    				    info.wShowWindow = SW_HIDE
    				    subprocess.Popen(r'loop5003.bat', startupinfo=info)
    				    t.sleep((delay/1000))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BubbleBoiLauncher = QtWidgets.QMainWindow()
    ui = Ui_BubbleBoiLauncher()
    ui.setupUi(BubbleBoiLauncher)
    BubbleBoiLauncher.show()
    sys.exit(app.exec_())
