from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from Frontend.FilterDesigner.Lista_Filtros import listaf
from analog.filters import *
import numpy as np
import os

from Frontend.FilterDesigner.mplwidget import MplWidget

from Frontend.FilterDesigner.stagewidget import StageWidget

from Frontend.FilterDesigner.MainWindow import Ui_MainWindow  # Se importa archivo generado por designer

from Frontend.FilterDesigner.Window2 import Ui_Window2

import sys

#Clase de ventana principal
class MainWindow(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        #Defino todos los callbacks de botones y demas
        self.ui.boton_agregar_filtro.clicked.connect(self.crear_filtro)

        self.ui.boton_borrar_filtro.clicked.connect(self.remover_filtro_lista)

        self.ui.boton_seleccionar_filtro.clicked.connect(self.seleccionar_filtro)

        self.ui.boton_graficar.clicked.connect(self.update_grafico)

        self.ui.boton_limpiar1.clicked.connect(lambda: self.clear_grafico(1))

        self.ui.boton_limpiar2.clicked.connect(lambda: self.clear_grafico(2))

        self.ui.boton_etapa2.clicked.connect(self.first_window)

        self.ui.selector_filtro.currentIndexChanged.connect(self.change_image)
        self.ui.selector_filtro.currentIndexChanged.connect(self.change_parameter_box)



    #crea los diferentes filtros y los agrega a las listas de la gui
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

            label = str(self.ui.input_maximo_Q.text())
            print(label)

            try:
                n = int(self.ui.input_orden_filtro.text())
                if n == 0:
                    n = None
            except:
                if n == 0:
                    n = None

            #Este try comprueba que el usuario haya creado bien el filtro
            try:
                if aprox == 'Butterworth':
                    filtro = Butterworth(tipo, wp, ws, Ap, As, ganancia, rp=0, k=k, N=n, name=label)
                    self.agregar_filtro_lista(filtro)
                    listaf.cambiar_label(label)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(filtro.get_order()))
                elif aprox == 'Chebycheff':
                    filtro = Chebyshev1(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n, name=label)
                    self.agregar_filtro_lista(filtro)
                    listaf.cambiar_label(label)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(filtro.get_order()))
                elif aprox == 'Chebycheff Inverso':
                    filtro = Chebyshev2(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n, name=label)
                    self.agregar_filtro_lista(filtro)
                    listaf.cambiar_label(label)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(filtro.get_order()))
                elif aprox == 'Legendre':
                    self.show_pop_up('not implemented')
                elif aprox == 'Gauss':
                    self.show_pop_up('not implemented')
                elif aprox == 'Cauer':
                    filtro = Cauer(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n, name=label)
                    self.agregar_filtro_lista(filtro)
                    listaf.cambiar_label(label)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(filtro.get_order()))
                else:
                    filtro = Bessel(tipo, wp, ws, Ap, As, ganancia, rp=0, k=0, N=n, name=label)
                    self.agregar_filtro_lista(filtro)
                    listaf.cambiar_label(label)
                    self.ui.lista_filtros.addItem(str(listaf.indice) + ')' + aprox + ' ' + tipo + ' orden ' + str(filtro.get_order()))
            except ValueError as error:
                self.show_pop_up(str(error))

        except ValueError:
            self.show_pop_up('Entrada vacía')

    #Remueve filtro de la lista de filtros visual de la gui
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

    #agrega filtro a la lista de la gui
    def agregar_filtro_lista(self, filtro): ##Agrega filtro a lista que se usa para llevar cuenta de filtros a graficar
        listaf.agregar_filtro(filtro)
        listaf.indice_up()

    #selecciona el filtro para poder graficarlo
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

    #updatea grafico el try es por compatibilidad de graficos
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

    #limpia ejes de graficos
    def clear_grafico(self, window):

        for f in listaf.lista_filtros:
            for key in f.is_graphed:
                if window == f.is_graphed[key][1]:
                    f.mark_not_graphed(key)

        if window == 1:
            self.ui.ventana_grafica1.clear_axes()
        else:
            self.ui.ventana_grafica2.clear_axes()

    #muestra pop up de advertencia
    def show_pop_up(self, error):
        msg = QMessageBox()
        msg.setWindowTitle('Mistakes were made')
        msg.setText(error)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

    #maneja uso de checkboxes
    def checkboxes(self, i, where):

        if self.ui.checkbox_plantilla.isChecked():
            listaf.lista_filtros[i].mark_graphed('Template', where)
        else:
            listaf.lista_filtros[i].mark_not_graphed('Template')

    #cambia imagens plantillas
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

    #cambia inputs para pasa banda y rechaza banda
    def change_parameter_box(self):

        if self.ui.selector_filtro.currentText() == 'Band-pass' or self.ui.selector_filtro.currentText() == 'Band-stop':
            self.ui.input_frecuencia_bpmenos.setEnabled(True)
            self.ui.input_frecuencia_brmenos.setEnabled(True)

        else:
            self.ui.input_frecuencia_bpmenos.setEnabled(False)
            self.ui.input_frecuencia_brmenos.setEnabled(False)


    #cambia de ventana
    def first_window(self):
        if len(listaf.lista_filtros):
            self.switch_window.emit()
        else:
            self.show_pop_up('To Acces the second window you must select a filter first.')

#clase correspondiente a ventana 2
class Window2(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, selected):
        super(Window2, self).__init__()
        self.ui = Ui_Window2()
        self.ui.setupUi(self)

        self.last_selected = -1
        self.stage_numbers = []

        self.stages_list = []
        self.selected_stage = 0

        self.selected = selected

        cells = self.selected.get_stages()
        self.celdas = []  #lista de listas con id mas la celda
        id = 1

        for cell in cells:
            self.celdas.append([id, cell])
            id += 1

        self.add_stages_list()
        self.set_pz()

        self.disable_zeros()

        self.ui.lista_polos.itemSelectionChanged.connect(lambda: self.select('polo'))
        self.ui.lista_ceros.itemSelectionChanged.connect(lambda: self.select('cero'))

        self.ui.boton_agregar_etapa.clicked.connect(self.add_stage)

        self.ui.boton_derecha.clicked.connect(self.etapa_derecha)

        self.ui.boton_izquierda.clicked.connect(self.etapa_izquierda)

        self.ui.boton_borrar_etapa.clicked.connect(self.delete_stage)

        self.ui.boton_etapas_automaticas.clicked.connect(self.auto_stages)

        self.ui.boton_reset.clicked.connect(self.reset)

        self.ui.boton_etapa1.clicked.connect(self.switch)

    #añade celdas a la lista
    def add_stages_list(self):
        for celda in self.celdas:
            if len(celda[1].get_poles()):
                polos = celda[1].get_poles()
                self.ui.lista_polos.addItem(str(celda[0]) + ' Polo Q = ' + str(round(celda[1].get_q(), 4)) + ' ubicacion:' + str(round(polos[0])))
                self.stage_numbers.append(celda[0])

            if len(celda[1].get_zeros()):
                ceros = celda[1].get_zeros()
                for cero in ceros:
                    self.ui.lista_ceros.addItem(str(celda[0]) + ' Cero con real = ' + str(round(cero.real, 4)) + ' imaginario = ' + str((cero.imag, 4)))
            else:
                self.ui.lista_ceros.addItem('None')

    #deshabilita selecionar ceros si no los hay
    def disable_zeros(self):
        item = self.ui.lista_ceros.item(0)
        if item.text() == 'None':
            self.ui.lista_ceros.setEnabled(False)
    #setea grafico polos y ceros
    def set_pz(self):
        for cell in self.celdas:
            self.ui.ventana_pz.plot_stage_pz(cell[1], 0.5)

    #selecciona una etapa y la grafica abajo
    def select(self, tipo):
        poles_and_zeros = False
        zeros_and_poles = False

        if tipo == 'polo':
            item_polo = self.ui.lista_polos.currentItem()
            value_polo = item_polo.text()
            ind = int(value_polo[0])

            for i in range(self.ui.lista_ceros.count()):
                item = self.ui.lista_ceros.item(i)
                if item.text()[0] == str(ind):
                    poles_and_zeros = True

        else:
            item_cero = self.ui.lista_ceros.currentItem()
            value_cero = item_cero.text()
            ind = int(value_cero[0])

            for i in range(self.ui.lista_polos.count()):
                item = self.ui.lista_polos.item(i)
                if item.text()[0] == str(ind):
                    zeros_and_poles = True


        et = None
        for cell in self.celdas:
            if cell[0] == ind:
                et = cell[1]

        if tipo == 'polo':
            slc = et.get_poles()
        else:
            slc = et.get_zeros()

        #bajo opacidad demas polos y ceros
        self.ui.ventana_pz.clear_axes()
        for cell in self.celdas:
            self.ui.ventana_pz.plot_stage_pz(cell[1], 0.2)


        #subo opacidad a lo que este seleccionado
        self.ui.ventana_pz.select_pz(slc, tipo)
        if poles_and_zeros:
            slc2 = et.get_zeros()
            self.ui.ventana_pz.select_pz(slc2, 'cero')
        else:
            slc2 = et.get_poles()
            self.ui.ventana_pz.select_pz(slc2, 'polo')



    #agrega la etapa
    def add_stage(self):

        item_polo = self.ui.lista_polos.currentItem()
        if item_polo is not None:
            value_polo = item_polo.text()
            ind = int(value_polo[0])

        item_cero = self.ui.lista_ceros.currentItem()
        if item_cero is not None:
            value_cero = item_cero.text()
            ind2 = int(value_cero[0])

        if ind in self.stage_numbers or ind2 in self.stage_numbers:

            if len(self.stages_list) < len(self.selected.get_stages()):

                self.selected_stage = 1

                itemp = self.ui.lista_polos.currentItem()
                textp = itemp.text()
                numberp = textp[0]

                celda = None
                for cell in self.celdas:
                    if cell[0] == int(numberp):
                        celda = cell[1]


                new_stage = Stages(celda.get_w(), celda.get_mag(), celda.get_q(), ind)
                print(celda.get_w())
                print(celda.get_mag())
                self.stages_list.append(new_stage)

                self.graph_stages()
                self.graph_total_transfer()
                print(ind)
                try:
                    self.stage_numbers.remove(ind)
                except ValueError:
                    self.stage_numbers.remove(ind2)
            else:
                self.show_popup('You cant add more stages because you reached the maximun given by your filter aproximation')
        else:
            self.show_popup('Stage already selected!')

    #grafica las etapas
    def graph_stages(self):
        #esto borra los widgets anteriores
        for i in reversed(range(self.ui.horizontalLayout_2.count())):
            self.ui.horizontalLayout_2.itemAt(i).widget().setParent(None)

        suma = 0
        for counter, stg in enumerate(self.stages_list):

            ventana = StageWidget(self.ui.marco_etapas)
            ventana.plot_mag(stg, name=f"Etapa {counter}")
            if counter + 1 == self.selected_stage:
                ventana.select()
            suma += stg.mag
            print(suma)

            ventana.setMaximumSize(QtCore.QSize(250, 300))
            self.ui.horizontalLayout_2.addWidget(ventana)

    #cambia a etapa derecha
    def etapa_derecha(self):
        if self.selected_stage < len(self.stages_list):
            self.selected_stage += 1
            self.graph_stages()

    #cambia a etapa izquierda
    def etapa_izquierda(self):
        if self.selected_stage != 1:
            self.selected_stage -= 1
            self.graph_stages()

    #borra etapa
    def delete_stage(self):
        self.stage_numbers.append(self.stages_list[self.selected_stage - 1].id)


        self.stages_list.pop(self.selected_stage - 1)
        self.selected_stage -= 1
        self.graph_stages()
        if not len(self.stages_list):
            self.ui.ventana_etapas.clear_axes()
            for celda in self.celdas:
                self.stage_numbers.append(celda[0])
        else:
            self.graph_total_transfer()




    #etapas automaticas
    def auto_stages(self):
        stgs = self.selected.get_stages()
        self.stages_list = []
        self.selected_stage = 1

        for s in stgs:
            etp = Stages(s.get_w(), s.get_mag(), s.get_q(), 0)
            self.stages_list.append(etp)

        self.graph_stages()
        self.graph_total_transfer()

    #reseta all
    def reset(self):
        self.stages_list = []
        self.selected_stage = 0
        self.graph_stages()
        self.ui.ventana_etapas.clear_axes()

    #muestra mensaje pop up si el usuario hizo algo mal
    def show_popup(self, error):
        msg = QMessageBox()
        msg.setWindowTitle('Mistakes were made')
        msg.setText(error)
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

    #grafica trasnferencia total
    def graph_total_transfer(self):
        if len(self.stages_list) == len(self.selected.get_stages()):
            self.ui.ventana_etapas.plot_stage2(self.selected.get_w(), self.selected.get_mag())
        else:
            mag = 0
            for stg in self.stages_list:
                mag += stg.mag
            print(1)
            self.ui.ventana_etapas.plot_stage2(self.selected.get_w(), mag)

    #cambio de ventana
    def switch(self):
        self.switch_window.emit()
        self.close()

    def get_label(self):
        return self.label

#clase etapa
class Stages:
    def __init__(self, w, mag, q, id):
        self.w = w
        self.mag = mag
        self.q = q
        self.id = id




# Controlador de ventanas, conecta señales que le dicen a las distintas ventanas cuando abrirse y cerrarse
class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.window.show()

    def show_window_two(self):
        print(listaf.seleccionado)
        print(listaf.lista_filtros[0].get_mag())
        self.window_two = Window2(listaf.lista_filtros[listaf.seleccionado])
        self.window.close()
        self.window_two.switch_window.connect(self.show_main)
        self.window_two.show()


#main
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
