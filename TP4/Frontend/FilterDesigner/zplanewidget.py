from PyQt5.QtWidgets import *
from  PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvas
from webcolors import *
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict


class ZplaneWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Esto detecta color background y se lo pone a la figura del grafico (asi es generico)
        color = self.palette().color(QtGui.QPalette.Background)
        color.red(), color.green(), color.blue()
        hex = rgb_to_hex((color.red(), color.green(), color.blue()))

        self.fig = Figure(figsize=(1, 1), facecolor=hex) #asi aparece cuadrado
        self.fig.savefig("image_filename.png", edgecolor=self.fig.get_edgecolor())

        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()

        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)

        self.setLayout(layout)

    def zplot(self, filtro):

        self.clear_axes()
        # Plot the poles and set marker properties
        for p in filtro.poles:
            poles = self.canvas.axes.plot(p.real, p.imag, 'x', markersize=9, color='blue', alpha=0.7)

        # Plot the zeros and set marker properties
        for z in filtro.zeros:
            zeros = self.canvas.axes.plot(z.real, z.imag, 'o', markersize=9, color='red', alpha=0.7)

        self.canvas.draw()

    def clear_axes(self):
        self.canvas.axes.clear()
        self.canvas.draw()