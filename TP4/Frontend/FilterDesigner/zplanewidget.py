from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

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

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()

        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111, )
        self.setLayout(layout)

    def zplot(self, filtro):


        # Plot the poles and set marker properties
        for p in filtro.poles:
            poles = self.canvas.axes.plot(p.real, p.imag, 'x', markersize=9, color='blue', alpha=0.5)

        # Plot the zeros and set marker properties
        for z in filtro.zeros:
            zeros = self.canvas.axes.plot(z.real, z.imag, 'o', markersize=9, color='red', alpha=0.5)

        self.canvas.draw()