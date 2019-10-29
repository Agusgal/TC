from PyQt5 import QtWidgets, QtGui
from Frontend.FilterDesigner.Lista_Filtros import  listaf
from analog.filters import *
import numpy as np


from Frontend.FilterDesigner.MainWindow import Ui_MainWindow  # Se importa archivo generado por designer

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.boton_agregar_filtro.clicked.connect(self.crear_filtro)

        self.ui.boton_borrar_filtro.clicked.connect(self.remover_filtro_lista)

        self.ui.boton_seleccionar_filtro.clicked.connect(self.seleccionar_filtro)

        self.ui.boton_graficar.clicked.connect(self.update_grafico)

        #self.ui.boton_limpiar.clicked.connect()

    def crear_filtro(self):  ##Conisderar que el usuario puede meter cosas mal, agregar chequeo errores

        aprox = self.ui.selector_aproximacion.currentText()

        if self.ui.selector_filtro.currentText() == 'Low-pass':
            tipo = 'lowpass'
        elif self.ui.selector_filtro.currentText() == 'High-pass':
            tipo = 'highpass'
        elif self.ui.selector_filtro.currentText() == 'Band-pass':
            tipo = 'bandpass'
        else:
            tipo = 'bandstop'

        wp = float(self.ui.input_frecuencia_bp.text()) * 2 * np.pi
        ws = float(self.ui.input_frecuencia_br.text()) * 2 * np.pi
        Ap = float(self.ui.input_atenuacion_bp.text())
        As = float(self.ui.input_atenuacion_br.text())
        ganancia = int(self.ui.input_ganancia.text())

        k = int(self.ui.input_desnormalizacion.text()) / 100

        n = int(self.ui.input_orden_filtro.text())

        try:
            if aprox == 'Butterworth':
                filtro = Butterworth(tipo, wp, ws, Ap, As, ganancia, rp=0, k=k, N=n)
                self.agregar_filtro_lista(filtro)
        except ValueError as error:
            print(error)

        self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + str(round(wp)) + ' ' + str(round(ws)) + ' ' + str(Ap) + ' ' + str(As) + ' ' + str(ganancia) + ' ' + str(k) + ' ' + str(n))

    def remover_filtro_lista(self):
        ##Agregar q pasa cuando no hay  nada seleccionado

        item = self.ui.lista_filtros.takeItem(self.ui.lista_filtros.currentRow())
        sitem = item.text()
        ind = int(sitem[0])
        listaf.borrar_filtro(ind)
        listaf.indice_down()
        item = None

    def agregar_filtro_lista(self, filtro): ##Agrega filtro a lista que se usa para llevar cuenta de filtros a graficar
        listaf.agregar_filtro(filtro)
        listaf.indice_up()

    def seleccionar_filtro(self):
        item = self.ui.lista_filtros.currentItem()
        value = item.text()
        self.ui.label_filtro_graficar.setText(value)

    def update_grafico(self):

        txt = self.ui.label_filtro_graficar.text()
        ind = int(txt[0])
        name = self.ui.selector_grafico.currentText()
        window = self.ui.selector_ventana.currentText()
        where = 0

        if window == 'Window 1':
            where = 1
        else:
            where = 2

        listaf.lista_filtros[ind].mark_graphed(name, where)

        self.ui.ventana_grafica1.plot(listaf.lista_filtros[ind])
        self.ui.ventana_grafica2.plot()

    def clear_grafico(self):
        for f in listaf.lista_filtros:
            for key in f.is_graphed:
                f.mark_not_graphed(key)

        self.ui.ventana_grafica1.clear_axes()
        self.ui.ventana_grafica2.clear_axes()

    def errores(self):
        pass




if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    application = MainWindow()
    application.show()

    sys.exit(app.exec())

