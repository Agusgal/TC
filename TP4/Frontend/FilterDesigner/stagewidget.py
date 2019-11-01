from PyQt5.QtWidgets import *
from  PyQt5 import QtGui
from webcolors import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas

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

        self.setLayout(layout)



