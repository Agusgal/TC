# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.marco_tipo_filtro = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_tipo_filtro.sizePolicy().hasHeightForWidth())
        self.marco_tipo_filtro.setSizePolicy(sizePolicy)
        self.marco_tipo_filtro.setMaximumSize(QtCore.QSize(280, 16777215))
        self.marco_tipo_filtro.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_tipo_filtro.setFlat(True)
        self.marco_tipo_filtro.setCheckable(False)
        self.marco_tipo_filtro.setObjectName("marco_tipo_filtro")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.marco_tipo_filtro)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.selector_filtro = QtWidgets.QComboBox(self.marco_tipo_filtro)
        self.selector_filtro.setObjectName("selector_filtro")
        self.selector_filtro.addItem("")
        self.selector_filtro.addItem("")
        self.selector_filtro.addItem("")
        self.selector_filtro.addItem("")
        self.gridLayout_6.addWidget(self.selector_filtro, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.marco_tipo_filtro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_6.addWidget(self.widget, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.marco_tipo_filtro, 0, 2, 1, 1)
        self.marco_graficos = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_graficos.sizePolicy().hasHeightForWidth())
        self.marco_graficos.setSizePolicy(sizePolicy)
        self.marco_graficos.setMaximumSize(QtCore.QSize(280, 16777215))
        self.marco_graficos.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_graficos.setObjectName("marco_graficos")
        self.gridLayout = QtWidgets.QGridLayout(self.marco_graficos)
        self.gridLayout.setObjectName("gridLayout")
        self.selector_ventana = QtWidgets.QComboBox(self.marco_graficos)
        self.selector_ventana.setObjectName("selector_ventana")
        self.selector_ventana.addItem("")
        self.selector_ventana.addItem("")
        self.gridLayout.addWidget(self.selector_ventana, 1, 1, 1, 1)
        self.selector_grafico = QtWidgets.QComboBox(self.marco_graficos)
        self.selector_grafico.setObjectName("selector_grafico")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.selector_grafico.addItem("")
        self.gridLayout.addWidget(self.selector_grafico, 1, 0, 1, 1)
        self.boton_graficar = QtWidgets.QPushButton(self.marco_graficos)
        self.boton_graficar.setObjectName("boton_graficar")
        self.gridLayout.addWidget(self.boton_graficar, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.marco_graficos, 0, 0, 2, 1)
        self.marco_filtros = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_filtros.sizePolicy().hasHeightForWidth())
        self.marco_filtros.setSizePolicy(sizePolicy)
        self.marco_filtros.setMaximumSize(QtCore.QSize(280, 16777215))
        self.marco_filtros.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_filtros.setObjectName("marco_filtros")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.marco_filtros)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.boton_borrar_filtro = QtWidgets.QPushButton(self.marco_filtros)
        self.boton_borrar_filtro.setObjectName("boton_borrar_filtro")
        self.gridLayout_5.addWidget(self.boton_borrar_filtro, 1, 1, 1, 1)
        self.boton_mostrar_filtro = QtWidgets.QPushButton(self.marco_filtros)
        self.boton_mostrar_filtro.setObjectName("boton_mostrar_filtro")
        self.gridLayout_5.addWidget(self.boton_mostrar_filtro, 1, 0, 1, 1)
        self.lista_filtros = QtWidgets.QListView(self.marco_filtros)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lista_filtros.sizePolicy().hasHeightForWidth())
        self.lista_filtros.setSizePolicy(sizePolicy)
        self.lista_filtros.setObjectName("lista_filtros")
        self.gridLayout_5.addWidget(self.lista_filtros, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.marco_filtros, 3, 2, 1, 1)
        self.marco_parametros = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_parametros.sizePolicy().hasHeightForWidth())
        self.marco_parametros.setSizePolicy(sizePolicy)
        self.marco_parametros.setMaximumSize(QtCore.QSize(280, 16777215))
        self.marco_parametros.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_parametros.setObjectName("marco_parametros")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.marco_parametros)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.marco_parametros)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 7, 2, 1, 1)
        self.label_frecuencia_bp = QtWidgets.QLabel(self.marco_parametros)
        self.label_frecuencia_bp.setObjectName("label_frecuencia_bp")
        self.gridLayout_3.addWidget(self.label_frecuencia_bp, 1, 0, 1, 1)
        self.label_atenuacion_br = QtWidgets.QLabel(self.marco_parametros)
        self.label_atenuacion_br.setObjectName("label_atenuacion_br")
        self.gridLayout_3.addWidget(self.label_atenuacion_br, 4, 0, 1, 1)
        self.label_dB_ganancia = QtWidgets.QLabel(self.marco_parametros)
        self.label_dB_ganancia.setObjectName("label_dB_ganancia")
        self.gridLayout_3.addWidget(self.label_dB_ganancia, 0, 2, 1, 1)
        self.input_ganancia = QtWidgets.QLineEdit(self.marco_parametros)
        self.input_ganancia.setObjectName("input_ganancia")
        self.gridLayout_3.addWidget(self.input_ganancia, 0, 1, 1, 1)
        self.input_atenuacion_bp = QtWidgets.QLineEdit(self.marco_parametros)
        self.input_atenuacion_bp.setObjectName("input_atenuacion_bp")
        self.gridLayout_3.addWidget(self.input_atenuacion_bp, 3, 1, 1, 1)
        self.label_Hz_br = QtWidgets.QLabel(self.marco_parametros)
        self.label_Hz_br.setObjectName("label_Hz_br")
        self.gridLayout_3.addWidget(self.label_Hz_br, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.marco_parametros)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 7, 1, 1, 1)
        self.label_Q_maximo = QtWidgets.QLabel(self.marco_parametros)
        self.label_Q_maximo.setObjectName("label_Q_maximo")
        self.gridLayout_3.addWidget(self.label_Q_maximo, 10, 0, 1, 1)
        self.label_ganancia = QtWidgets.QLabel(self.marco_parametros)
        self.label_ganancia.setObjectName("label_ganancia")
        self.gridLayout_3.addWidget(self.label_ganancia, 0, 0, 1, 1)
        self.label_frecuencia_br = QtWidgets.QLabel(self.marco_parametros)
        self.label_frecuencia_br.setObjectName("label_frecuencia_br")
        self.gridLayout_3.addWidget(self.label_frecuencia_br, 2, 0, 1, 1)
        self.label_orden_filtro = QtWidgets.QLabel(self.marco_parametros)
        self.label_orden_filtro.setObjectName("label_orden_filtro")
        self.gridLayout_3.addWidget(self.label_orden_filtro, 9, 0, 1, 1)
        self.label_dB_atenuacion_bp = QtWidgets.QLabel(self.marco_parametros)
        self.label_dB_atenuacion_bp.setObjectName("label_dB_atenuacion_bp")
        self.gridLayout_3.addWidget(self.label_dB_atenuacion_bp, 3, 2, 1, 1)
        self.label_dB_atenuacion_br = QtWidgets.QLabel(self.marco_parametros)
        self.label_dB_atenuacion_br.setObjectName("label_dB_atenuacion_br")
        self.gridLayout_3.addWidget(self.label_dB_atenuacion_br, 4, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.marco_parametros)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 10, 1, 1, 1)
        self.input_frecuencia_bp = QtWidgets.QLineEdit(self.marco_parametros)
        self.input_frecuencia_bp.setObjectName("input_frecuencia_bp")
        self.gridLayout_3.addWidget(self.input_frecuencia_bp, 1, 1, 1, 1)
        self.label_desnormalizacion = QtWidgets.QLabel(self.marco_parametros)
        self.label_desnormalizacion.setObjectName("label_desnormalizacion")
        self.gridLayout_3.addWidget(self.label_desnormalizacion, 7, 0, 1, 1)
        self.label_atenuacion_bp = QtWidgets.QLabel(self.marco_parametros)
        self.label_atenuacion_bp.setObjectName("label_atenuacion_bp")
        self.gridLayout_3.addWidget(self.label_atenuacion_bp, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.marco_parametros)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 9, 1, 1, 1)
        self.input_frecuencia_br = QtWidgets.QLineEdit(self.marco_parametros)
        self.input_frecuencia_br.setObjectName("input_frecuencia_br")
        self.gridLayout_3.addWidget(self.input_frecuencia_br, 2, 1, 1, 1)
        self.input_atenuacion_br = QtWidgets.QLineEdit(self.marco_parametros)
        self.input_atenuacion_br.setObjectName("input_atenuacion_br")
        self.gridLayout_3.addWidget(self.input_atenuacion_br, 4, 1, 1, 1)
        self.label_Hz_bp = QtWidgets.QLabel(self.marco_parametros)
        self.label_Hz_bp.setObjectName("label_Hz_bp")
        self.gridLayout_3.addWidget(self.label_Hz_bp, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.marco_parametros, 1, 2, 1, 1)
        self.marco_aproximacion = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_aproximacion.sizePolicy().hasHeightForWidth())
        self.marco_aproximacion.setSizePolicy(sizePolicy)
        self.marco_aproximacion.setMaximumSize(QtCore.QSize(280, 16777215))
        self.marco_aproximacion.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_aproximacion.setObjectName("marco_aproximacion")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.marco_aproximacion)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.selector_aproximacion = QtWidgets.QComboBox(self.marco_aproximacion)
        self.selector_aproximacion.setObjectName("selector_aproximacion")
        self.selector_aproximacion.addItem("")
        self.selector_aproximacion.addItem("")
        self.selector_aproximacion.addItem("")
        self.selector_aproximacion.addItem("")
        self.selector_aproximacion.addItem("")
        self.selector_aproximacion.addItem("")
        self.selector_aproximacion.addItem("")
        self.gridLayout_4.addWidget(self.selector_aproximacion, 0, 0, 1, 1)
        self.boton_agregar_filtro = QtWidgets.QPushButton(self.marco_aproximacion)
        self.boton_agregar_filtro.setObjectName("boton_agregar_filtro")
        self.gridLayout_4.addWidget(self.boton_agregar_filtro, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.marco_aproximacion, 2, 2, 1, 1)
        self.marco_edicion_graficos = QtWidgets.QGroupBox(self.centralwidget)
        self.marco_edicion_graficos.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.marco_edicion_graficos.setObjectName("marco_edicion_graficos")
        self.gridLayout_2.addWidget(self.marco_edicion_graficos, 2, 0, 2, 1)
        self.ventana_grafica1 = MplWidget(self.centralwidget)
        self.ventana_grafica1.setObjectName("ventana_grafica1")
        self.gridLayout_2.addWidget(self.ventana_grafica1, 0, 1, 2, 1)
        self.ventana_grafica2 = MplWidget(self.centralwidget)
        self.ventana_grafica2.setObjectName("ventana_grafica2")
        self.gridLayout_2.addWidget(self.ventana_grafica2, 2, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.marco_tipo_filtro.setTitle(_translate("MainWindow", "Type of Filter:"))
        self.selector_filtro.setItemText(0, _translate("MainWindow", "Low-pass"))
        self.selector_filtro.setItemText(1, _translate("MainWindow", "High-pass"))
        self.selector_filtro.setItemText(2, _translate("MainWindow", "Band_pass"))
        self.selector_filtro.setItemText(3, _translate("MainWindow", "Band_stop"))
        self.marco_graficos.setTitle(_translate("MainWindow", "GroupBox"))
        self.selector_ventana.setItemText(0, _translate("MainWindow", "Window 1"))
        self.selector_ventana.setItemText(1, _translate("MainWindow", "Window 2"))
        self.selector_grafico.setItemText(0, _translate("MainWindow", "Template"))
        self.selector_grafico.setItemText(1, _translate("MainWindow", "Attenuation"))
        self.selector_grafico.setItemText(2, _translate("MainWindow", "Magnitude"))
        self.selector_grafico.setItemText(3, _translate("MainWindow", "Phase"))
        self.selector_grafico.setItemText(4, _translate("MainWindow", "Group Delay"))
        self.selector_grafico.setItemText(5, _translate("MainWindow", "Maximun Q"))
        self.selector_grafico.setItemText(6, _translate("MainWindow", "Impulse Response"))
        self.selector_grafico.setItemText(7, _translate("MainWindow", "Step Response"))
        self.selector_grafico.setItemText(8, _translate("MainWindow", "Poles and Zeroes"))
        self.boton_graficar.setText(_translate("MainWindow", "Graph"))
        self.marco_filtros.setTitle(_translate("MainWindow", "Filters"))
        self.boton_borrar_filtro.setText(_translate("MainWindow", "Remove"))
        self.boton_mostrar_filtro.setText(_translate("MainWindow", "Show"))
        self.marco_parametros.setTitle(_translate("MainWindow", "Filter Configuration:"))
        self.label_2.setText(_translate("MainWindow", "%"))
        self.label_frecuencia_bp.setText(_translate("MainWindow", "Passband Frequency (Fp):"))
        self.label_atenuacion_br.setText(_translate("MainWindow", "Stopband Attenuation(Aa):"))
        self.label_dB_ganancia.setText(_translate("MainWindow", "dB"))
        self.label_Hz_br.setText(_translate("MainWindow", "Hz"))
        self.label_Q_maximo.setText(_translate("MainWindow", "Maximun Q:"))
        self.label_ganancia.setText(_translate("MainWindow", "Gain:"))
        self.label_frecuencia_br.setText(_translate("MainWindow", "Stopband Frequency(Fa):"))
        self.label_orden_filtro.setText(_translate("MainWindow", "Filter Order:"))
        self.label_dB_atenuacion_bp.setText(_translate("MainWindow", "dB"))
        self.label_dB_atenuacion_br.setText(_translate("MainWindow", "dB"))
        self.label_desnormalizacion.setText(_translate("MainWindow", "Denormalization"))
        self.label_atenuacion_bp.setText(_translate("MainWindow", "Passband Attenuation(Ap):"))
        self.label_Hz_bp.setText(_translate("MainWindow", "Hz"))
        self.marco_aproximacion.setTitle(_translate("MainWindow", "Aproximation:"))
        self.selector_aproximacion.setItemText(0, _translate("MainWindow", "Butterworth"))
        self.selector_aproximacion.setItemText(1, _translate("MainWindow", "Bessel"))
        self.selector_aproximacion.setItemText(2, _translate("MainWindow", "Chebycheff"))
        self.selector_aproximacion.setItemText(3, _translate("MainWindow", "Chebycheff Inverso"))
        self.selector_aproximacion.setItemText(4, _translate("MainWindow", "Legendre"))
        self.selector_aproximacion.setItemText(5, _translate("MainWindow", "Gauss"))
        self.selector_aproximacion.setItemText(6, _translate("MainWindow", "Cauer"))
        self.boton_agregar_filtro.setText(_translate("MainWindow", "Add Filter"))
        self.marco_edicion_graficos.setTitle(_translate("MainWindow", "Aca va edicion de graficos"))

from mplwidget import MplWidget
