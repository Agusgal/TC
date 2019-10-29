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

    def plot(self, filtro):

        for key in filtro.is_graphed:
            if filtro.is_graphed[key]:
                if key == 'template':
                    pass
                elif key == 'mag':
                    self.canvas.axes.semilogx(filtro.get_w(), filtro.get_mag())
                    self.canvas.draw()
                elif key =='phase':
                    pass
                elif key == 'g delay':
                    pass
                elif key == 'max Q':
                    pass
                elif key == 'impulse resp':
                    pass
                elif key == 'step resp':
                    pass
                elif key == 'poles and zeroes':
                    pass

    def clear_axes(self):
        self.canvas.axes.clear()
