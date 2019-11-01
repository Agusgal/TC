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
        Window2.resize(1217, 870)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Window2.sizePolicy().hasHeightForWidth())
        Window2.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Window2)
        self.gridLayout.setObjectName("gridLayout")
        self.marco_edicion_etapas = QtWidgets.QGroupBox(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_edicion_etapas.sizePolicy().hasHeightForWidth())
        self.marco_edicion_etapas.setSizePolicy(sizePolicy)
        self.marco_edicion_etapas.setMaximumSize(QtCore.QSize(380, 16777215))
        self.marco_edicion_etapas.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_edicion_etapas.setObjectName("marco_edicion_etapas")
        self.gridLayout.addWidget(self.marco_edicion_etapas, 0, 0, 5, 1)
        self.ventana_etapas = MplWidget(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ventana_etapas.sizePolicy().hasHeightForWidth())
        self.ventana_etapas.setSizePolicy(sizePolicy)
        self.ventana_etapas.setMaximumSize(QtCore.QSize(700, 16777215))
        self.ventana_etapas.setObjectName("ventana_etapas")
        self.gridLayout.addWidget(self.ventana_etapas, 0, 1, 1, 1)
        self.marco_setup = QtWidgets.QGroupBox(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_setup.sizePolicy().hasHeightForWidth())
        self.marco_setup.setSizePolicy(sizePolicy)
        self.marco_setup.setMaximumSize(QtCore.QSize(16777215, 80))
        self.marco_setup.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_setup.setObjectName("marco_setup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.marco_setup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_izquierda = QtWidgets.QPushButton(self.marco_setup)
        self.boton_izquierda.setObjectName("boton_izquierda")
        self.horizontalLayout.addWidget(self.boton_izquierda)
        self.boton_borrar_etapa = QtWidgets.QPushButton(self.marco_setup)
        self.boton_borrar_etapa.setObjectName("boton_borrar_etapa")
        self.horizontalLayout.addWidget(self.boton_borrar_etapa)
        self.boton_derecha = QtWidgets.QPushButton(self.marco_setup)
        self.boton_derecha.setObjectName("boton_derecha")
        self.horizontalLayout.addWidget(self.boton_derecha)
        self.gridLayout.addWidget(self.marco_setup, 4, 1, 1, 1)
        self.marco_pz = QtWidgets.QGroupBox(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_pz.sizePolicy().hasHeightForWidth())
        self.marco_pz.setSizePolicy(sizePolicy)
        self.marco_pz.setMaximumSize(QtCore.QSize(380, 16777215))
        self.marco_pz.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_pz.setObjectName("marco_pz")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.marco_pz)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lista_ceros = QtWidgets.QListWidget(self.marco_pz)
        self.lista_ceros.setEnabled(True)
        self.lista_ceros.setMaximumSize(QtCore.QSize(16777215, 75))
        self.lista_ceros.setObjectName("lista_ceros")
        self.gridLayout_2.addWidget(self.lista_ceros, 3, 2, 1, 1)
        self.ventana_pz = StageWidget(self.marco_pz)
        self.ventana_pz.setMaximumSize(QtCore.QSize(375, 375))
        self.ventana_pz.setObjectName("ventana_pz")
        self.gridLayout_2.addWidget(self.ventana_pz, 1, 1, 1, 2)
        self.label_ceros = QtWidgets.QLabel(self.marco_pz)
        self.label_ceros.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_ceros.setObjectName("label_ceros")
        self.gridLayout_2.addWidget(self.label_ceros, 2, 2, 1, 1)
        self.boton_agregar_etapa = QtWidgets.QPushButton(self.marco_pz)
        self.boton_agregar_etapa.setObjectName("boton_agregar_etapa")
        self.gridLayout_2.addWidget(self.boton_agregar_etapa, 4, 1, 1, 1)
        self.label_polos = QtWidgets.QLabel(self.marco_pz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_polos.sizePolicy().hasHeightForWidth())
        self.label_polos.setSizePolicy(sizePolicy)
        self.label_polos.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_polos.setObjectName("label_polos")
        self.gridLayout_2.addWidget(self.label_polos, 2, 1, 1, 1)
        self.lista_polos = QtWidgets.QListWidget(self.marco_pz)
        self.lista_polos.setEnabled(True)
        self.lista_polos.setMaximumSize(QtCore.QSize(16777215, 75))
        self.lista_polos.setObjectName("lista_polos")
        self.gridLayout_2.addWidget(self.lista_polos, 3, 1, 1, 1)
        self.boton_etapas_automaticas = QtWidgets.QPushButton(self.marco_pz)
        self.boton_etapas_automaticas.setObjectName("boton_etapas_automaticas")
        self.gridLayout_2.addWidget(self.boton_etapas_automaticas, 4, 2, 1, 1)
        self.boton_etapa1 = QtWidgets.QPushButton(self.marco_pz)
        self.boton_etapa1.setObjectName("boton_etapa1")
        self.gridLayout_2.addWidget(self.boton_etapa1, 5, 1, 1, 2)
        self.gridLayout.addWidget(self.marco_pz, 0, 2, 5, 1)
        self.marco_etapas = QtWidgets.QGroupBox(Window2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_etapas.sizePolicy().hasHeightForWidth())
        self.marco_etapas.setSizePolicy(sizePolicy)
        self.marco_etapas.setMaximumSize(QtCore.QSize(16777215, 200))
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.marco_etapas)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addWidget(self.marco_etapas, 5, 0, 1, 3)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "Form"))
        self.marco_edicion_etapas.setTitle(_translate("Window2", "Stage Edition"))
        self.marco_setup.setTitle(_translate("Window2", "Stage Set-up"))
        self.boton_izquierda.setText(_translate("Window2", "Left Stage"))
        self.boton_borrar_etapa.setText(_translate("Window2", "Delete Stage"))
        self.boton_derecha.setText(_translate("Window2", "Right Stage"))
        self.marco_pz.setTitle(_translate("Window2", "Poles and Zeroes"))
        self.label_ceros.setText(_translate("Window2", "Zeros"))
        self.boton_agregar_etapa.setText(_translate("Window2", "Add Stage"))
        self.label_polos.setText(_translate("Window2", "Poles"))
        self.boton_etapas_automaticas.setText(_translate("Window2", "Automatic Stages"))
        self.boton_etapa1.setText(_translate("Window2", "PushButton"))
        self.marco_etapas.setTitle(_translate("Window2", "Stages"))

from mplwidget import MplWidget
from stagewidget import StageWidget
