# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window2(object):
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(1329, 883)
        self.boton_etapa1 = QtWidgets.QPushButton(Window2)
        self.boton_etapa1.setGeometry(QtCore.QRect(580, 370, 113, 32))
        self.boton_etapa1.setObjectName("boton_etapa1")

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "Form"))
        self.boton_etapa1.setText(_translate("Window2", "atras"))

