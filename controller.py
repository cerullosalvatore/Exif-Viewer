from View.view import *
from Model.model import *
from View.windowResizable import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QFileDialog, QShortcut
import webbrowser
"""
Questa classe rappresenta il Controller del programma.
"""
class Controller:
    def __init__(self):
        self._window = Window()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self._window)
        self._model = modelImagesExiff()
        self._window.setWindowTitle("Exif Viewer")

        #Inizializzo le azioni
        self.setAction()
        #Inizializzo i listeners
        self.setRegister()
        #Inizializzo i comandi rapidi
        self.setShortcut()
        #Visualizzo la finestra
        self._window.show()
        #Imposto la finestra al centro dello schermo
        self._window.center()

    def setAction(self):
        #Imposto le azioni per gli elementi della GUI che generano eventi
        self._ui.pushButton.clicked.connect(lambda: self.loadImageAction())
        self._ui.pushButton_4.clicked.connect(lambda: self._model.changeImage("-"))
        self._ui.pushButton_5.clicked.connect(lambda: self._model.changeImage("+"))
        self._ui.pushButton_3.clicked.connect(lambda: self._model.rotateImageOf90())
        self._ui.pushButton_2.clicked.connect(self.goToMap)

    def setShortcut(self):
        #Imposto le azioni per le scorciatoie della GUI che generano eventi
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self._ui.pushButton_3)
        self.shortcut.activated.connect(lambda: self._model.rotateImageOf90())
        self.shortcut1 = QShortcut(QKeySequence("Ctrl+M"), self._ui.pushButton_2)
        self.shortcut1.activated.connect(self.goToMap)
        self.shortcut2 = QShortcut(QKeySequence("left"), self._ui.pushButton_4)
        self.shortcut2.activated.connect(lambda: self._model.changeImage("-"))
        self.shortcut3 = QShortcut(QKeySequence("right"), self._ui.pushButton_5)
        self.shortcut3.activated.connect(lambda: self._model.changeImage("+"))

    def setRegister(self):
        #Imposto i listener della gui agli oggetti del modello
        self._model.setRegisterImages(lambda: self.updateImage(0))
        self._model.setRegisterId(lambda x: self.updateImage(x))
        self._model.setRegisterRotate(lambda x: self.rotateImage(x))
        self._model.setRegisterMap(lambda x: self._ui.pushButton_2.setEnabled(x))
        self._window.resized.connect(lambda: self.rotateImage(self._model.getRotate()))

    def loadImageAction(self):
        """
        Effettua le operazioni di caricamento delle immagini filtrando solo quelle di tipo .jpg
        """
        self._model.loadImages(QFileDialog.getOpenFileNames(self._window, "Select one or more files to open", "/home", "Images (*.jpg)")[0])

    def updateImage(self, x):
        """
        Effettua l'update dell'immagine corrente, aggiornando gli exif e la visualizzazione dell'immagine
        :param x: immagine
        """
        if self._model.getLength() > 0:
            self._model.loadCurrentImage()
            self._ui.pushButton_3.setEnabled(True)
            self._ui.pushButton_4.setEnabled(False)
            self._ui.pushButton_5.setEnabled(False)
            self._ui.label_2.setEnabled(True)
            self._ui.label_3.setEnabled(True)
            self._ui.tableWidget.setEnabled(True)
            self._ui.label_2.setText(str(x + 1) + " / " + str(self._model.getLength()))
            pixmap = QtGui.QPixmap(self._model.getCurrentImagePath())
            pixmap = self.resizeFunction(pixmap)
            self._ui.label.setPixmap(pixmap)
            self.compileExiffTable()
            if self._model.getLength() > 1:
                self._ui.pushButton_4.setEnabled(True)
                self._ui.pushButton_5.setEnabled(True)

    def rotateImage(self, x):
        """
        Ruota l'immagine
        :param x:
        """
        t = QtGui.QTransform()
        t.rotate(x)
        rotated_pixmap = QtGui.QPixmap(self._model.getCurrentImagePath()).transformed(t)
        rescaled_pixmap = self.resizeFunction(rotated_pixmap)
        self._ui.label.setPixmap(rescaled_pixmap)

    def goToMap(self):
        """
        Apre una nuova scheda all'interno del browser collegandosi a googleMaps e mostrando il luogo in cui è stata scattata
        la fotografia
        """
        webbrowser.open(self._model.getUrlMap(), new=2)

    def resizeFunction(self, original_pixmap):
        """
        Effettua le operazioni di resize dell'immagine mantenendo il rapporto originale quando la dimensione della finestra viene modificata
        :param original_pixmap:
        :return:
        """
        resized_pixmap = original_pixmap
        if(original_pixmap.width() > self._ui.widget_9.width() or original_pixmap.height() > self._ui.widget_9.height()):
            resized_pixmap = original_pixmap.scaled(self._ui.widget_9.width(),
                                                    self._ui.widget_9.height(),
                                                    QtCore.Qt.KeepAspectRatio,
                                                    QtCore.Qt.FastTransformation)
        return resized_pixmap

    def compileExiffTable(self):
        """
        Compila la tabella dei tag exif dell'immagine corrente
        """
        while self._ui.tableWidget.rowCount() > 0:
            self._ui.tableWidget.removeRow(0)

        if self._model.getExiff() != None:
            for x in self._model.getExiff():
                row_pos = self._ui.tableWidget.rowCount()
                self._ui.tableWidget.insertRow(row_pos)
                self._ui.tableWidget.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(x))
                self._ui.tableWidget.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(self._model.getExiff()[x])))

        self._ui.tableWidget.resizeColumnToContents(0)
        self._ui.tableWidget.resizeColumnToContents(1)