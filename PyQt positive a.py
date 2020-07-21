import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.a = 4.00

        self.initUI()

        self.setLayout(self.layout)
        self.setGeometry(200, 200, 800, 600)

    def initUI(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.slider = QSlider(Qt.Horizontal,self)


        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.set_a)
        self.slider.sliderMoved.connect(self.doGraph1)

        self.doGraph1()

        self.layout = layout

    def set_a(self,x):
        self.a = 4 + (x / 100)

    def doGraph1(self):
        self.fig.clear()

        ax = self.fig.add_subplot(111, projection='3d')
        ax.set_zlabel('real domain')
        ax.set_ylabel('imaginarly domain')
        ax.set_xlabel('real range')
        ax.set_ylim(-10000,+10000)
        ax.set_zlim(-10000,+10000)

        x_space = np.linspace(-10, +10, 400)
        i_space = np.array([])
        r_space = np.array([])
        a = self.a
        for p in range(len(x_space)):
            if p == int(len(x_space) / 2):
                i = np.inf
                r = np.inf
            elif x_space[p] < 0:
                i = (-x_space[p]) ** a * np.sin(np.pi * a)
                r = (-x_space[p]) ** a * np.cos(np.pi * a)
            elif x_space[p] > 0:
                i = 0
                r = x_space[p] ** a

            i_space = np.append(i_space, [i])
            r_space = np.append(r_space, [r])


        ax.plot(x_space, i_space, r_space, label="a={0}".format(a))

        ax.legend()

        self.canvas.draw()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()