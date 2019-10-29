# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(layout)

    def plot(self, lista_filtros):
        
        for filtro in lista_filtros:
            for key in filtro.is_graphed:
                if filtro.is_graphed[key][0]:
                    if key == 'template':
                        pass
                    elif key == 'Magnitude':
                        self.canvas.axes.semilogx(filtro.get_w(), filtro.get_mag())
                        self.canvas.draw()
                    elif key == 'Phase':
                        pass
                    elif key == 'Group Delay':
                        pass
                    elif key == 'Maximun Q':
                        pass
                    elif key == 'Impulse Response':
                        pass
                    elif key == 'Step Response':
                        pass
                    elif key == 'Poles and Zeroes':
                        pass

    def clear_axes(self):
        self.canvas.axes.clear()
