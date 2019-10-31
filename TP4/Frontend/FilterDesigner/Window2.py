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
        self.gridLayout = QtWidgets.QGridLayout(Window2)
        self.gridLayout.setObjectName("gridLayout")
        self.marco_etapas = QtWidgets.QGroupBox(Window2)
        self.marco_etapas.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_etapas.setObjectName("marco_etapas")
        self.gridLayout.addWidget(self.marco_etapas, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 1))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.boton_etapa1 = QtWidgets.QPushButton(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_etapa1.sizePolicy().hasHeightForWidth())
        self.boton_etapa1.setSizePolicy(sizePolicy)
        self.boton_etapa1.setMinimumSize(QtCore.QSize(250, 0))
        self.boton_etapa1.setObjectName("boton_etapa1")
        self.gridLayout.addWidget(self.boton_etapa1, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Window2)
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.boton_etapas_automaticas = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_etapas_automaticas.setObjectName("boton_etapas_automaticas")
        self.gridLayout_2.addWidget(self.boton_etapas_automaticas, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Window2)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.ventana_etapas = MplWidget(Window2)
        self.ventana_etapas.setObjectName("ventana_etapas")
        self.gridLayout.addWidget(self.ventana_etapas, 0, 1, 3, 1)
        self.widget = QtWidgets.QWidget(Window2)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 3)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "Form"))
        self.marco_etapas.setTitle(_translate("Window2", "Stage Configuration"))
        self.groupBox.setTitle(_translate("Window2", "GroupBox"))
        self.boton_etapa1.setText(_translate("Window2", "PushButton"))
        self.groupBox_3.setTitle(_translate("Window2", "Poles and Zeroes"))
        self.boton_etapas_automaticas.setText(_translate("Window2", "Create Stages Automatically"))
        self.groupBox_2.setTitle(_translate("Window2", "GroupBox"))

from mplwidget import MplWidget
