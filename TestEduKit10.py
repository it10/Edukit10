# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boton.ui'
#
# Created: Wed Jun 22 15:04:41 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import conexionUSB
import serial
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import date, datetime, timedelta
from smtplib import SMTP
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
#global arduino = serial.Serial()
class MiHilo(threading.Thread):
    def run (self):
        arduino.write("0x0d");
        arduino.write("Interruptores\n")
        inte = arduino.read()
        print (inte)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(639, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 641, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        #Primer pestaña LEDS
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        #LAYOUT CONTENEDOR DE CHECKBOX
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 10, 111, 291))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        #1° CHECKBOX LEDS2
        #LEDS2
        self.CheckLeds2 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckLeds2.setObjectName(_fromUtf8("CheckLeds2"))
        self.verticalLayout_2.addWidget(self.CheckLeds2)
        #2° CHECKBOX LEDS3
        #LEDS3
        self.CheckLeds3 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckLeds3.setObjectName(_fromUtf8("CheckLeds3"))
        self.verticalLayout_2.addWidget(self.CheckLeds3)
        #3° CHECKBOX LEDS4
        #LEDS4
        self.CheckLeds3_2 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckLeds3_2.setObjectName(_fromUtf8("CheckLeds3_2"))
        self.verticalLayout_2.addWidget(self.CheckLeds3_2)
        #4° CHECKBOX LEDS7
        #LEDS7
        self.CheckLeds7 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckLeds7.setObjectName(_fromUtf8("CheckLeds7"))
        self.verticalLayout_2.addWidget(self.CheckLeds7)
        #5° CHECKBOX LEDS8
        #LEDS8
        self.CheckLeds8 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckLeds8.setObjectName(_fromUtf8("CheckLeds8"))
        self.verticalLayout_2.addWidget(self.CheckLeds8)
        #6° CHECKBOX LEDS9
        #LEDS9
        self.CheckLeds9 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckLeds9.setObjectName(_fromUtf8("CheckLeds9"))
        self.verticalLayout_2.addWidget(self.CheckLeds9)
        #LAYOUT CONTENEDOR DE BOTONES
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 300, 178, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #BOTON OFF LEDS
        self.offLeds = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.offLeds.setObjectName(_fromUtf8("offLeds"))
        self.offLeds.clicked.connect(self.offleds_Click)
        self.horizontalLayout.addWidget(self.offLeds)
        #BOTON ON LEDS
        self.onLeds = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.onLeds.setObjectName(_fromUtf8("onLeds"))
        self.onLeds.clicked.connect(self.onleds_Click)
        self.horizontalLayout.addWidget(self.onLeds)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        #Segunda Pestaña ServoMotor
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.tab_4)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(170, 50, 160, 80))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        #LIneEDit Servo10
        self.gradosServo10 = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.gradosServo10.setObjectName(_fromUtf8("gradosServo10"))
        self.verticalLayout_3.addWidget(self.gradosServo10)
        #LineEdit Servo11
        self.gradosServo11 = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.gradosServo11.setObjectName(_fromUtf8("gradosServo11"))
        self.verticalLayout_3.addWidget(self.gradosServo11)
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.tab_4)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(330, 50, 160, 80))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        #Boton Girar Servo 10
        self.botonGirarServ10 = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.botonGirarServ10.setObjectName(_fromUtf8("botonGirarServ10"))
        self.verticalLayout_7.addWidget(self.botonGirarServ10)
        self.botonGirarServ10.clicked.connect(self.girarServo10)
        #Boton Girar Servo 11
        self.botonGirarServ11 = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.botonGirarServ11.setObjectName(_fromUtf8("botonGirarServ11"))
        self.botonGirarServ11.clicked.connect(self.girarServo11)
        self.verticalLayout_7.addWidget(self.botonGirarServ11)
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.tab_4)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 50, 160, 80))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_8.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        #Tercera Pestaña Motor
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(40, 20, 231, 251))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        #Boton Girar Motor Izquierdo
        self.GirarMotorIzq = QtGui.QPushButton(self.verticalLayoutWidget_9)
        self.GirarMotorIzq.setObjectName(_fromUtf8("GirarMotorIzq"))
        self.horizontalLayout_3.addWidget(self.GirarMotorIzq)
        self.GirarMotorIzq.clicked.connect(self.girarMotorI)
        #Boton Frenar Motor Izquierdo
        self.FrenarMotorIzq = QtGui.QPushButton(self.verticalLayoutWidget_9)
        self.FrenarMotorIzq.setObjectName(_fromUtf8("FrenarMotorIzq"))
        self.FrenarMotorIzq.clicked.connect(self.frenarMotorI)
        self.horizontalLayout_3.addWidget(self.FrenarMotorIzq)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_10 = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(340, 20, 231, 251))
        self.verticalLayoutWidget_10.setObjectName(_fromUtf8("verticalLayoutWidget_10"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_10)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        #Boton Girar Motor Derecho
        self.GirarMotorDer = QtGui.QPushButton(self.verticalLayoutWidget_10)
        self.GirarMotorDer.setObjectName(_fromUtf8("GirarMotorDer"))
        self.GirarMotorDer.clicked.connect(self.girarMotorD)
        self.horizontalLayout_4.addWidget(self.GirarMotorDer)
        #Boton Girar Motor Derecho
        self.FrenarMotorDer = QtGui.QPushButton(self.verticalLayoutWidget_10)
        self.FrenarMotorDer.setObjectName(_fromUtf8("FrenarMotorDer"))
        self.FrenarMotorDer.clicked.connect(self.frenarMotorD)
        self.horizontalLayout_4.addWidget(self.FrenarMotorDer)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        #Cuarta Pestaña Ldr
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_5)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 100, 170, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        #Ldc Panel 
        self.lcdLdr = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.lcdLdr.setObjectName(_fromUtf8("lcdLdr"))
        self.horizontalLayout_2.addWidget(self.lcdLdr)
        #BOton Obtener Valor LDR
        self.ldr_obtenerValor = QtGui.QPushButton(self.tab_5)
        self.ldr_obtenerValor.setGeometry(QtCore.QRect(320, 120, 141, 51))
        self.ldr_obtenerValor.setObjectName(_fromUtf8("ldr_obtenerValor"))
        self.ldr_obtenerValor.clicked.connect(self.obtenerValorLDR)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        #Quinta Pestaña
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 30, 311, 221))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        #LINEEDIT TIme
        self.lineEdit_Time = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Time.setObjectName(_fromUtf8("lineEdit_Time"))
        self.verticalLayout.addWidget(self.lineEdit_Time)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        #LINEEDIT FRECUENCIA
        self.lineEdit_Frecuencia = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Frecuencia.setObjectName(_fromUtf8("lineEdit_Frecuencia"))
        self.verticalLayout.addWidget(self.lineEdit_Frecuencia)
        #BOTON ENCENDER BOCINA
        self.Bocina = QtGui.QPushButton(self.tab_2)
        self.Bocina.setGeometry(QtCore.QRect(120, 290, 309, 27))
        self.Bocina.setObjectName(_fromUtf8("Bocina"))
        self.Bocina.clicked.connect(self.encenderBocina)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        #Sexta Pestaña Interruptores
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab_6)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(60, 40, 160, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lcd_Interruptor10 = QtGui.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_Interruptor10.setObjectName(_fromUtf8("lcd_Interruptor10"))
        self.verticalLayout_4.addWidget(self.lcd_Interruptor10)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.tab_6)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(60, 150, 160, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lcd_Interruptor11 = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.lcd_Interruptor11.setObjectName(_fromUtf8("lcd_Interruptor11"))
        self.verticalLayout_5.addWidget(self.lcd_Interruptor11)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.tab_6)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(60, 250, 160, 80))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lcd_Interruptor12 = QtGui.QLCDNumber(self.verticalLayoutWidget_5)
        self.lcd_Interruptor12.setObjectName(_fromUtf8("lcd_Interruptor12"))
        self.verticalLayout_6.addWidget(self.lcd_Interruptor12)
        self.label_3 = QtGui.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(240, 60, 121, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(240, 170, 121, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(240, 270, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        #Boton Probar Interruptores
        self.botonProbarInt = QtGui.QPushButton(self.tab_6)
        self.botonProbarInt.setGeometry(QtCore.QRect(220, 0, 85, 27))
        self.botonProbarInt.setObjectName(_fromUtf8("botonProbarInt"))
        self.botonProbarInt.clicked.connect(self.probarInterruptores)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.listarPuertos = QtGui.QComboBox(self.centralwidget)
        self.listarPuertos.setGeometry(QtCore.QRect(150, 0, 121, 31))
        self.listarPuertos.setObjectName(_fromUtf8("listarPuertos"))
        self.buscarPuertos = QtGui.QPushButton(self.centralwidget)
        self.buscarPuertos.setGeometry(QtCore.QRect(20, 0, 101, 27))
        self.buscarPuertos.setObjectName(_fromUtf8("buscarPuertos"))
        self.buscarPuertos.clicked.connect(self.buspuertos)
	self.listarPuertos.currentIndexChanged.connect(self.selectedUsb)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buspuertos(self):
        a=conexionUSB.devconn()

        b = a.split(' ')
        self.listarPuertos.clear()
        for i in b:
            self.listarPuertos.addItem(i)
        self.listarPuertos.currentIndexChanged.connect(self.selectedUsb)

    def selectedUsb(self):
        global arduino
        current_Text = self.listarPuertos.currentText()
        print (current_Text)
        arduino = serial.Serial(str(current_Text), 9600)
        #return arduino

    def offleds_Click(self):
        #puerto="/dev/{0}".format +(os.system("tail  /var/log/syslog | grep 'ch341-uart converter now attached to ' | awk '{print $NF}'"))
        #print (puerto)
        #arduino = serial.Serial(puerto, 9600, timeout = 3.0)
        #for x in range(0, 5):
        if self.CheckLeds2.isChecked():
            arduino.write('Leds2\n')
        if self.CheckLeds3.isChecked():
            arduino.write('Leds3\n')
        if self.CheckLeds3_2.isChecked():
            arduino.write('Leds4\n')
        if self.CheckLeds7.isChecked():
            arduino.write('Leds7\n')
        if self.CheckLeds8.isChecked():
            arduino.write('Leds8\n')
        if self.CheckLeds9.isChecked():
            arduino.write('Leds9\n')
        #arduino.close()

    def onleds_Click(self):
        if self.CheckLeds2.isChecked():
            arduino.write('OnLeds2\n')
        if self.CheckLeds3.isChecked():
            arduino.write('OnLeds3\n')
        if self.CheckLeds3_2.isChecked():
            arduino.write('OnLeds4\n')
        if self.CheckLeds7.isChecked():
            arduino.write('OnLeds7\n')
        if self.CheckLeds8.isChecked():
            arduino.write('OnLeds8\n')
        if self.CheckLeds9.isChecked():
            arduino.write('OnLeds9\n')

    def obtenerValorLDR(self):
        self.lcdLdr.display('0')
        arduino.flushInput()
        arduino.flushOutput()
        #valor = 0
        arduino.write('LDR\n')
        time.sleep(.1)
        #valor = arduino.readline()
        #print(valor)
        self.lcdLdr.display(arduino.readline())


    def girarServo10(self):
        arduino.write('girarServo10\n')
        #arduino.write(self.gradosServo10.text())
        print(self.gradosServo10.text())

    def girarServo11(self):
        arduino.write('girarServo11\n')
        #arduino.write(self.gradosServo11.text())
        print(self.gradosServo11.text())

    def girarMotorI(self):
        arduino.write('GirarMotorIzqr\n')

    def frenarMotorI(self):
        arduino.write('FrenarMotorIzq\n') 

    def girarMotorD(self):
        arduino.write('GirarMotorDer\n')

    def frenarMotorD(self):
        arduino.write('FrenarMotorDer\n')

    def encenderBocina(self):
        print (self.lineEdit_Frecuencia.text())
        print (self.lineEdit_Time.text())
        arduino.write('Bocina\n')

    def probarInterruptores(self):
        self.lcd_Interruptor10.display('0')
        self.lcd_Interruptor11.display('0')
        self.lcd_Interruptor12.display('0')
        arduino.flushInput()
        arduino.flushOutput()
        arduino.write('Interruptores\n')
        boton=''
        time.sleep(.1)
        boton = arduino.readline()
        print(boton)
        if(boton=="10\r\n"):
            self.lcd_Interruptor10.display('5 ')
        if(boton=="11\r\n"):
            self.lcd_Interruptor11.display('5 ')
        if(boton=="12\r\n"):
            self.lcd_Interruptor12.display('5 ')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IT10-Edukit", None))
        self.CheckLeds2.setText(_translate("MainWindow", "Leds 2", None))
        self.CheckLeds3.setText(_translate("MainWindow", "Leds 3", None))
        self.CheckLeds3_2.setText(_translate("MainWindow", "Leds 4", None))
        self.CheckLeds7.setText(_translate("MainWindow", "Leds 7", None))
        self.CheckLeds8.setText(_translate("MainWindow", "Leds 8", None))
        self.CheckLeds9.setText(_translate("MainWindow", "Leds 9", None))
        self.offLeds.setText(_translate("MainWindow", "On Leds", None))
        self.onLeds.setText(_translate("MainWindow", "Off Leds", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Leds", None))
        self.botonGirarServ10.setText(_translate("MainWindow", "Girar Servo 10", None))
        self.botonGirarServ11.setText(_translate("MainWindow", "Girar Servo 11", None))
        self.label_7.setText(_translate("MainWindow", "Servo Motor 10", None))
        self.label_8.setText(_translate("MainWindow", "Servo Motor 11", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Servo Motor", None))
        self.label_9.setText(_translate("MainWindow", "Girar Izquierda", None))
        self.label_10.setText(_translate("MainWindow", "Girar Derecha", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Servo Motor", None))
        self.label_9.setText(_translate("MainWindow", "                    Girar Izquierda", None))
        self.GirarMotorIzq.setText(_translate("MainWindow", "Girar", None))
        self.FrenarMotorIzq.setText(_translate("MainWindow", "Frenar", None))
        self.label_10.setText(_translate("MainWindow", "                    Girar Derecha", None))
        self.GirarMotorDer.setText(_translate("MainWindow", "Girar", None))
        self.FrenarMotorDer.setText(_translate("MainWindow", "Frenar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Motor", None))
        self.ldr_obtenerValor.setText(_translate("MainWindow", "Obtener valor ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "LDR", None))
        self.label.setText(_translate("MainWindow", "Time", None))
        self.label_2.setText(_translate("MainWindow", "Frecuencia", None))
        self.Bocina.setText(_translate("MainWindow", "Sonar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bocina", None))
        self.label_3.setText(_translate("MainWindow", "Interruptor D10", None))
        self.label_4.setText(_translate("MainWindow", "Interruptor D11", None))
        self.label_5.setText(_translate("MainWindow", "Interruptor D12", None))
        self.botonProbarInt.setText(_translate("MainWindow", "Probar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Interruptores", None))
        
        self.buscarPuertos.setText(_translate("MainWindow", "Buscar Puertos", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

