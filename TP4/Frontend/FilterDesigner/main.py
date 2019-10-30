from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
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

        self.ui.boton_limpiar1.clicked.connect(lambda: self.clear_grafico(1))

        self.ui.boton_limpiar2.clicked.connect(lambda: self.clear_grafico(2))

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

        wp = None
        ws = None
        Ap = None
        As = None
        ganancia = None
        k = None
        n = None

        try:
            wp = float(self.ui.input_frecuencia_bp.text()) * 2 * np.pi
            ws = float(self.ui.input_frecuencia_br.text()) * 2 * np.pi
            Ap = float(self.ui.input_atenuacion_bp.text())
            As = float(self.ui.input_atenuacion_br.text())
            ganancia = int(self.ui.input_ganancia.text())

            k = int(self.ui.input_desnormalizacion.text()) / 100

            n = int(self.ui.input_orden_filtro.text())

            try:  # falta agregar otro tipos de errores
                if aprox == 'Butterworth':
                    filtro = Butterworth(tipo, wp, ws, Ap, As, ganancia, rp=0, k=k, N=n)
                    self.agregar_filtro_lista(filtro)
                    self.ui.lista_filtros.addItem(
                        str(listaf.indice) + ')' + aprox + ' ' + str(round(wp)) + ' ' + str(round(ws)) + ' ' + str(
                            Ap) + ' ' + str(As) + ' ' + str(ganancia) + ' ' + str(k) + ' ' + str(n))
            except ValueError as error:
                self.show_pop_up(str(error))

        except ValueError:
            self.show_pop_up('Entrada vacía')

        #########try: #falta agregar otro tipos de errores
           ######## if aprox == 'Butterworth':
              #######  filtro = Butterworth(tipo, wp, ws, Ap, As, ganancia, rp=0, k=k, N=n)
              ######  self.agregar_filtro_lista(filtro)
             #####   self.ui.lista_filtros.addItem(
              ####      str(listaf.indice) + ')' + aprox + ' ' + str(round(wp)) + ' ' + str(round(ws)) + ' ' + str(
              ###          Ap) + ' ' + str(As) + ' ' + str(ganancia) + ' ' + str(k) + ' ' + str(n))
        ##except ValueError as error:
        #    self.show_pop_up(str(error))


    def remover_filtro_lista(self):
        ##Agregar q pasa cuando no hay  nada seleccionado
        try:
            item = self.ui.lista_filtros.takeItem(self.ui.lista_filtros.currentRow())
            sitem = item.text()
            ind = int(sitem[0])
            listaf.borrar_filtro(ind)
            listaf.indice_down()
            item = None

            self.ui.ventana_polos_zeros.clear_axes()
        except AttributeError:
            self.show_pop_up('Debe seleccionar algún filtro de la lista!')

    def agregar_filtro_lista(self, filtro): ##Agrega filtro a lista que se usa para llevar cuenta de filtros a graficar
        listaf.agregar_filtro(filtro)
        listaf.indice_up()

    def seleccionar_filtro(self):

        try:
            item = self.ui.lista_filtros.currentItem()
            value = item.text()
            self.ui.label_filtro_graficar.setText(value)
            ind = int(value[0]) - 1
            where = 3

            listaf.lista_filtros[ind].mark_graphed('Poles and Zeroes', where)
            self.ui.ventana_polos_zeros.plot(listaf.lista_filtros)
        except AttributeError:
            self.show_pop_up('Debe Seleccionar algun filtro de la lista!')

    def update_grafico(self):

        txt = self.ui.label_filtro_graficar.text()
        ind = int(txt[0]) - 1
        name = self.ui.selector_grafico.currentText()
        window = self.ui.selector_ventana.currentText()
        where = 0

        if window == 'Window 1':
            where = 1
        else:
            where = 2

        listaf.lista_filtros[ind].mark_graphed(name, where)

        self.ui.ventana_grafica1.plot(listaf.lista_filtros)

        self.ui.ventana_grafica2.plot(listaf.lista_filtros)

    def clear_grafico(self, window):

        for f in listaf.lista_filtros:
            for key in f.is_graphed:
                if window == f.is_graphed[key][1]:
                    f.mark_not_graphed(key)

        if window == 1:
            self.ui.ventana_grafica1.clear_axes()
        else:
            self.ui.ventana_grafica2.clear_axes()

    def limpiar_entradas(self):
        pass

    def show_pop_up(self, error):
        msg = QMessageBox()
        msg.setWindowTitle('Mistakes were made')
        msg.setText(error)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    application = MainWindow()
    application.show()

    sys.exit(app.exec())

