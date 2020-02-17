from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtCore import pyqtSignal

class Window(QMainWindow):
    resized = pyqtSignal()
    def  __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def center(self):
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        self.move(qr.topLeft())