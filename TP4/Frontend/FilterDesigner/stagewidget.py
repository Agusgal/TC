from PyQt5.QtWidgets import *
from  PyQt5 import QtGui
from webcolors import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas

import numpy as np

class StageWidget(QWidget):

    def __init__(self, identificador=0, parent=None):
        QWidget.__init__(self, parent)

        # Esto detecta color background y se lo pone a la figura del grafico (asi es generico)
        color = self.palette().color(QtGui.QPalette.Background)
        color.red(), color.green(), color.blue()
        hex = rgb_to_hex((color.red(), color.green(), color.blue()))

        self.fig = Figure(figsize=(1, 1), facecolor=hex)  # asi aparece cuadrado
        self.fig.savefig("image_filename.png", edgecolor=self.fig.get_edgecolor())

        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()

        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_facecolor("#e1ddbf")

        self.setLayout(layout)

    def plot_stage_pz(self, stage, opacity):
        zeros = stage.get_zeros()
        poles = stage.get_poles()


        for z in zeros:
            self.canvas.axes.scatter(z.real, z.imag, c='red', marker='o', alpha=opacity)
            self.canvas.draw()
        for p in poles:
            self.canvas.axes.scatter(p.real, p.imag, c='blue', marker='x', alpha=opacity)
            self.canvas.draw()

    def select_pz(self, selected, tipo):
        if tipo == 'polo':
            mark = 'x'
            color = 'blue'
        else:
            mark = 'o'
            color = 'red'

        for x in selected:
            self.canvas.axes.scatter(x.real, x.imag, c=color, marker=mark, alpha=1)
            self.canvas.draw()

    def plot_mag(self, stage, name):
        self.canvas.axes.semilogx(np.divide(stage.w, 2 * np.pi), stage.mag, color='blue', label=name)
        self.canvas.draw()

    def select(self):
        self.canvas.axes.spines['top'].set_color('red')
        self.canvas.axes.spines['top'].set_linewidth(2)

        self.canvas.axes.spines['bottom'].set_color('red')
        self.canvas.axes.spines['bottom'].set_linewidth(2)

        self.canvas.axes.spines['right'].set_color('red')
        self.canvas.axes.spines['right'].set_linewidth(2)

        self.canvas.axes.spines['left'].set_color('red')
        self.canvas.axes.spines['left'].set_linewidth(2)

        self.canvas.draw()

    def clear_axes(self):
        self.canvas.axes.clear()