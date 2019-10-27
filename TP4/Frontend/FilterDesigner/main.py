from PyQt5 import QtWidgets, QtGui
from Lista_Filtros import *
from analog_copy.filters import *
from numpy import pi

from MainWindow import Ui_MainWindow  # importing our generated file

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.boton_agregar_filtro.connect(self.crear_filtro)


    def crear_filtro(self):
        ##Conisderar que el usuario puede meter cosas mal, agregar chequeo errores

        tipo = self.ui.selector_filtro.currentText()
        wp = int(self.ui.input_frecuencia_bp.text()) * 2 * pi
        ws = int(self.ui.input_frecuencia_br.text()) * 2 * pi
        Ap = int(self.ui.input_atenuacion_bp.text())
        As = int(self.ui.input_atenuacion_br.text())
        ganancia = int(self.ui.input_ganancia.text())

        if self.ui.selector_aproximacion.currentText() == 'Butterworth':
            filtro = Butterworth(tipo, wp, ws, Ap, As, ganancia, rp=0,  )

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    application = MainWindow()
    application.show()

    sys.exit(app.exec())
