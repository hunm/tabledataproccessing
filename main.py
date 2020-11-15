#!-*-coding:utf-8-*-
import sys
import pandas as pd
import design
import os
# import PyQt5 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from qtstyles import StylePicker
import plotly.graph_objects as go


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Access to variables, methods
        # and other in design.py
        super().__init__()
        self.setupUi(self)  # Design initialization
        self.btnBrowse.clicked.connect(self.browse_folder)



    def browse_folder(self, path):
        wb_patch = QFileDialog.getOpenFileName()[0]
        table = pd.read_excel(wb_patch)
        x = table.values[:, 0]
        y = table.values[:, 1]
        fig = go.Figure(data=go.Scatter(x = x, y = y))
        fig.show()

def main():
    app = QApplication(sys.argv)  # New instance QApplication
    window = ExampleApp()  # Create class object ExampleApp
    app.setStyleSheet(StylePicker("qdark").get_sheet())  # <-- changing the style here
    window.show()  # Show window
    app.exec_()  # and run application

if __name__ == '__main__':  # If we launch file directly, not importing
    main()  # run main()