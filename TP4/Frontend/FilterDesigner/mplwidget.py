# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from PyQt5 import QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np

from webcolors import *
from scipy import signal

from analog.filters import Chebyshev1


class MplWidget(QWidget):

    def __init__(self, identificador=0, parent=None):
        QWidget.__init__(self, parent)

        # Esto detecta color background y se lo pone a la figura del grafico (asi es generico)
        color = self.palette().color(QtGui.QPalette.Background)
        color.red(), color.green(), color.blue()
        hex = rgb_to_hex((color.red(), color.green(), color.blue()))

        self.fig = Figure(facecolor=hex)
        self.fig.savefig("image_filename.png", edgecolor=self.fig.get_edgecolor())

        self.canvas = FigureCanvas(self.fig)

        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_facecolor("#e1ddbf")
        self.setLayout(layout)

        self.id = identificador

    def plot(self, lista_filtros):

        self.canvas.axes.clear()
        for filtro in lista_filtros:
            for key in filtro.is_graphed:
                if filtro.is_graphed[key][0] and filtro.is_graphed[key][1] == self.id:
                    if key == 'Template' and  self.check_compatibility(filtro, key):
                        stencils = filtro.get_stencils(np.divide(filtro.get_w(), 2 * np.pi), -filtro.get_mag())
                        for s in stencils:
                            self.canvas.axes.fill(s[0], s[1], '1', lw=0)  # Set line-
                            self.canvas.draw()
                    elif key == 'Attenuation' and self.check_compatibility(filtro, key):
                        self.canvas.axes.semilogx(np.divide(filtro.get_w(), 2 * np.pi), -filtro.get_mag())
                        self.canvas.draw()
                    elif key == 'Magnitude' and self.check_compatibility(filtro, key):
                        self.canvas.axes.semilogx(np.divide(filtro.get_w(), 2 * np.pi), filtro.get_mag())
                        self.canvas.draw()
                    elif key == 'Phase' and self.check_compatibility(filtro, key):
                        self.canvas.axes.semilogx(np.divide(filtro.get_w(), 2 * np.pi), filtro.get_pha())
                        self.canvas.draw()
                    elif key == 'Group Delay' and self.check_compatibility(filtro, key):
                        w, gdelay = filtro.get_gdelay()
                        self.canvas.axes.semilogx(np.divide(w, gdelay))
                        self.canvas.draw()
                    elif key == 'Maximun Q' and self.check_compatibility(filtro, key):
                        pass
                    elif key == 'Impulse Response' and self.check_compatibility(filtro, key):
                        T, yout = filtro.get_impulse_response()
                        self.canvas.axes.plot(T, yout)
                        self.canvas.draw()
                        pass
                    elif key == 'Step Response' and self.check_compatibility(filtro, key):
                        T, yout = filtro.get_step()
                        self.canvas.axes.plot(T, yout)
                        self.canvas.draw()
                    elif key == 'Poles and Zeroes':
                        for z in filtro.zeros:
                            self.canvas.axes.scatter(z.real, z.imag, c='red', marker='o')
                            self.canvas.draw()
                        for p in filtro.poles:
                            self.canvas.axes.scatter(p.real, p.imag, c='blue', marker='x')
                            self.canvas.draw()

    def plot_stage2(self, w, mag):
        self.clear_axes()
        self.canvas.axes.semilogx(np.divide(w, 2 * np.pi), mag)
        self.canvas.draw()

    def clear_axes(self):
        self.canvas.axes.clear()
        self.canvas.draw()

    def check_compatibility(self, filtro, key): #retorna error si no es compatible con algun grafico

        if key == 'Template':
            for den in filtro.is_graphed:
                if den != 'Template' and den != 'Attenuation' and den != 'Poles and Zeroes':
                    if filtro.is_graphed[den][0]:
                        filtro.is_graphed[den][0] = 0
                        raise ValueError("Can't plot " + den + 'and template at the same time as it is only made for attenuation.' )
            return True

        elif key == 'Attenuation':
            for den in filtro.is_graphed:
                if den != 'Template' and den != 'Magnitude' and den != 'Attenuation' and den != 'Poles and Zeroes':
                    if filtro.is_graphed[den][0]:
                        filtro.is_graphed[den][0] = 0
                        raise ValueError('Graphs are not compatible, axes are diferent.')
            return True

        elif key == 'Magnitude':
            for den in filtro.is_graphed:
                if den == 'Template' and den != 'Poles and Zeroes':
                    if filtro.is_graphed[den][0]:
                        filtro.is_graphed[den][0] = 0
                        raise("Can't plot template and magitude as it is only made for attenuation.")

                elif den != 'Magnitude' and den != 'Attenuation' and den != 'Poles and Zeroes':
                    if filtro.is_graphed[den][0]:
                        filtro.is_graphed[den][0] = 0
                        raise ValueError('Graphs are not compatible, axes are diferent.')
            return True

        elif key == 'Phase':
            for den in filtro.is_graphed:
                if den != 'Phase' and den != 'Poles and Zeroes':
                    if filtro.is_graphed[den][0]:
                        filtro.is_graphed[den][0] = 0
                        raise ValueError('Graphs are not compatible.')
            return True

        elif key == 'Group Delay' or key == 'Step Response' or key == 'Impulse Response':
            for den in filtro.is_graphed:
                if den != 'Group Delay' and den != 'Step Response' and den != 'Impulse Response' and den != 'Poles and Zeroes':
                    if filtro.is_graphed[den][0]:
                        filtro.is_graphed[den][0] = 0
                        raise ValueError('Graphs are not compatible.')
            return True



