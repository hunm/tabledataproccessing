#!-*-coding:utf-8-*-
import sys
import pandas as pd
import random
# import PyQt5 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PySide2.QtCore import *
#(Ui_MainWindow, QMainWindow) = uic.loadUiType('interface.ui')
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

import matplotlib.pyplot as plt




class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 1920
        self.height = 1080
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)


        self.show()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=200):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(444)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        #data = [random.random() for i in range(25)]

        df = pd.read_excel(r'./data.xlsx', sheet_name='Лист1')

        x = df.values[:, 0]
        y = df.values[:, 1]
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        #plt.figure(figsize=(15, 7))
        #df.plot(x, y, 'r-')
        #plt.draw()
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())