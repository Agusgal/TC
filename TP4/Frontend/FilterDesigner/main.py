from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from Frontend.FilterDesigner.Lista_Filtros import listaf
from analog.filters import *
import numpy as np
import os

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

        self.ui.selector_filtro.currentIndexChanged.connect(self.change_image)
        self.ui.selector_filtro.currentIndexChanged.connect(self.change_parameter_box)

    def crear_filtro(self):

        aprox = self.ui.selector_aproximacion.currentText()
        wp = None
        ws = None
        Ap = None
        As = None
        ganancia = None
        k = None
        n = None

        try:
            if self.ui.selector_filtro.currentText() == 'Low-pass':
                tipo = 'lowpass'
                wp = float(self.ui.input_frecuencia_bp.text()) * 2 * np.pi
                ws = float(self.ui.input_frecuencia_br.text()) * 2 * np.pi
            elif self.ui.selector_filtro.currentText() == 'High-pass':
                tipo = 'highpass'
                wp = float(self.ui.input_frecuencia_bp.text()) * 2 * np.pi
                ws = float(self.ui.input_frecuencia_br.text()) * 2 * np.pi
            elif self.ui.selector_filtro.currentText() == 'Band-pass':  # Agregar que el amrco de parametros cambie a los que tiene que tener
                tipo = 'bandpass'
                self.change_parameter_box()
                wp = [float(self.ui.input_frecuencia_bpmenos.text()), float(self.ui.input_frecuencia_bp.text())]
                ws = [float(self.ui.input_frecuencia_brmenos.text()), float(self.ui.input_frecuencia_br.text())]
                print(1)
            else:
                tipo = 'bandstop'
                self.change_parameter_box()
                wp = [float(self.ui.input_frecuencia_bpmenos.text()), float(self.ui.input_frecuencia_bp.text())]
                ws = [float(self.ui.input_frecuencia_brmenos.text()), float(self.ui.input_frecuencia_br.text())]

            Ap = float(self.ui.input_atenuacion_bp.text())
            As = float(self.ui.input_atenuacion_br.text())
            ganancia = float(self.ui.input_ganancia.text())

            k = float(self.ui.input_desnormalizacion.text()) / 100

            n = int(self.ui.input_orden_filtro.text())

            #Todo agregar los demas filtros que tincho estuvo haciendo
            try:
                if aprox == 'Butterworth':
                    filtro = Butterworth(tipo, wp, ws, Ap, As, ganancia, rp=0, k=k, N=n)
                    print(2)
                    self.agregar_filtro_lista(filtro)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(n))
                elif aprox == 'Chebycheff':
                    filtro = Chebyshev1(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n)
                    self.agregar_filtro_lista(filtro)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(n))
                elif aprox == 'Chebycheff Inverso':
                    filtro = Chebyshev2(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n)
                    self.agregar_filtro_lista(filtro)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(n))
                elif aprox == 'Legendre':
                    pass
                elif aprox == 'gauss':
                    pass
                elif aprox == 'Cauer':
                    filtro = Cauer(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n)
                    self.agregar_filtro_lista(filtro)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(n))
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
            self.show_pop_up('You must select a filter from the list')

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
            print(ind)

            listaf.lista_filtros[ind].mark_graphed('Poles and Zeroes', where)
            self.ui.ventana_polos_zeros.zplot(listaf.lista_filtros[ind])
        except AttributeError:
            self.show_pop_up('You Must select a Filter from the list')

    def update_grafico(self):
        try:
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
        except ValueError as error:
            print(1)
            self.show_pop_up(str(error))

    def clear_grafico(self, window):

        for f in listaf.lista_filtros:
            for key in f.is_graphed:
                if window == f.is_graphed[key][1]:
                    f.mark_not_graphed(key)

        if window == 1:
            self.ui.ventana_grafica1.clear_axes()
        else:
            self.ui.ventana_grafica2.clear_axes()

    def show_pop_up(self, error):
        msg = QMessageBox()
        msg.setWindowTitle('Mistakes were made')
        msg.setText(error)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

    def checkboxes(self, i, where):

        if self.ui.checkbox_plantilla.isChecked():
            listaf.lista_filtros[i].mark_graphed('Template', where)
        else:
            listaf.lista_filtros[i].mark_not_graphed('Template')

    def change_image(self):
        path = os.path.dirname(os.path.abspath(__file__))
        path += '/Recursos'

        if self.ui.selector_filtro.currentText() == 'Low-pass':
            self.ui.label_imagen.setPixmap(QtGui.QPixmap(os.path.join(path, 'PasaBajo.png')))
        elif self.ui.selector_filtro.currentText() == 'High-pass':
            self.ui.label_imagen.setPixmap(QtGui.QPixmap(os.path.join(path, 'PasaAlto.png')))
        elif self.ui.selector_filtro.currentText() == 'Band-pass':
            self.ui.label_imagen.setPixmap(QtGui.QPixmap(os.path.join(path, 'PasaBanda.png')))
        else:
            self.ui.label_imagen.setPixmap(QtGui.QPixmap(os.path.join(path, 'RechazaBanda.png')))

    def change_parameter_box(self):#AORDENAR BIEN VENTANAS Y HACER QUE VUELVNA A LA NORMALIDAD

        if self.ui.selector_filtro.currentText() == 'Band-pass' or self.ui.selector_filtro.currentText() == 'Band-stop':
            self.ui.input_frecuencia_bpmenos.setEnabled(True)
            self.ui.input_frecuencia_brmenos.setEnabled(True)

        else:
            self.ui.input_frecuencia_bpmenos.setEnabled(False)
            self.ui.input_frecuencia_brmenos.setEnabled(False)



    def first_window(self):
        if listaf.seleccionado:
            self.switch_window.emit()
        else:
            self.show_pop_up('To Acces the second window you must select a filter first.')


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
