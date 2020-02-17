import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
from controller import *
from View.windowResizable import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Controller()
    app.exec_()
