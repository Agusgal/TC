# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np

from scipy import signal

from analog.filters import Chebyshev1

class MplWidget(QWidget):

    def __init__(self, identificador=0, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(layout)

        self.id = identificador

    def plot(self, lista_filtros):


        #Falta agregar compatibilidad entre tipos de graficos
        self.canvas.axes.clear()
        for filtro in lista_filtros:
            for key in filtro.is_graphed:
                if filtro.is_graphed[key][0] and filtro.is_graphed[key][1] == self.id:
                    if key == 'Template':
                        stencils = filtro.get_stencils(np.divide(filtro.get_w(), 2 * np.pi), -filtro.get_mag())
                        for s in stencils:
                            self.canvas.axes.fill(s[0], s[1], '1', lw=0)  # Set line-
                            self.canvas.draw()
                    elif key == 'Attenuation':
                        self.canvas.axes.semilogx(np.divide(filtro.get_w(), 2 * np.pi), -filtro.get_mag())
                        self.canvas.draw()
                    elif key == 'Magnitude':
                        self.canvas.axes.semilogx(np.divide(filtro.get_w(), 2 * np.pi), filtro.get_mag())
                        self.canvas.draw()
                    elif key == 'Phase':
                        self.canvas.axes.semilogx(np.divide(filtro.get_w(), 2 * np.pi), filtro.get_pha())
                        self.canvas.draw()
                    elif key == 'Group Delay':
                        w, gdelay = filtro.get_gdelay()
                        self.canvas.axes.semilogx(np.divide(w, gdelay))
                        self.canvas.draw()
                    elif key == 'Maximun Q':
                        pass
                    elif key == 'Impulse Response':
                        T, yout = filtro.gte_impulse()
                        self.canvas.axes.plot(T, yout)
                        self.canvas.draw()
                        pass
                    elif key == 'Step Response':
                        T, yout = filtro.get_step(filtro.sys)
                        self.canvas.axes.plot(T, yout)
                        self.canvas.draw()
                    elif key == 'Poles and Zeroes':
                        for z in filtro.zeros:
                            self.canvas.axes.scatter(z.real, z.imag, c='red', marker='o')
                            self.canvas.draw()
                        for p in filtro.poles:
                            self.canvas.axes.scatter(p.real, p.imag, c='blue', marker='x')
                            self.canvas.draw()

    def clear_axes(self):
        self.canvas.axes.clear()
        self.canvas.draw()

    def check_compatibility(self):
        pass