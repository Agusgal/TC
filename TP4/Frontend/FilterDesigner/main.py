from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from Frontend.FilterDesigner.Lista_Filtros import  listaf
from analog.filters import *
import numpy as np


from Frontend.FilterDesigner.MainWindow import Ui_MainWindow  # Se importa archivo generado por designer

from Frontend.FilterDesigner.Window2 import Ui_Window2

import sys


class MainWindow(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

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

        self.ui.boton_etapa2.clicked.connect(self.first_window)

    def crear_filtro(self):

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
                        str(listaf.indice) + ')' + aprox + ' orden ' + str(n) + ' ' + str(round(wp)) + ' ' + str(round(ws)) + ' ' + str(
                            Ap) + ' ' + str(As) + ' ' + str(ganancia) + ' ' + str(k))
                elif aprox == 'Chebycheff':
                    filtro = Chebyshev1(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n)
                    self.agregar_filtro_lista(filtro)
                    self.ui.lista_filtros.addItem(
                        str(listaf.indice) + ')' + aprox + ' orden ' + str(n) + ' ' + str(round(wp)) + ' ' + str(
                            round(ws)) + ' ' + str(
                            Ap) + ' ' + str(As) + ' ' + str(ganancia) + ' ' + str(k))
                elif aprox == 'Chebycheff Inverso':
                    pass
                elif aprox == 'Legendre':
                    pass
                elif aprox == 'gauss':
                    pass
                elif aprox == 'Cauer':
                    pass
                else:
                    pass
            except ValueError as error:
                self.show_pop_up(str(error))

        except ValueError:
            self.show_pop_up('Entrada vacía')


    def remover_filtro_lista(self):
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
            listaf.seleccionar(ind)

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

        self.checkboxes(ind, where)
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

    def checkboxes(self, i, where):

        if self.ui.checkbox_plantilla.isChecked():
            listaf.lista_filtros[i].mark_graphed('Template', where)

    def first_window(self):
        self.switch_window.emit()


class Window2(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Window2, self).__init__()
        self.ui = Ui_Window2()
        self.ui.setupUi(self)
        # agregar callbacks y metodos de botones

        self.ui.boton_etapa1.clicked.connect(self.switch)

    def switch(self):
        self.switch_window.emit()

# Controlador de ventanas, conecta señales que le dicen a las distintas ventanas cuando abrirse y cerrarse
class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.window.show()

    def show_window_two(self):
        self.window_two = Window2()
        self.window.close()
        self.window_two.switch_window.connect(self.show_main)
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
