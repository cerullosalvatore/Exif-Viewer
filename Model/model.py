from Model.observableImage import *
from Model.observableList import *

"""
La classe modelImagesExiff rappresenta il modello del programma.

Un oggetto di questa classe avrà due oggetti:
* _images: è un oggetto ObservableList che conterrà tutte le immagini caricate .jpg nel programma.
* _currentImmage: è un oggetto ObservableImage che rappresenta l'immagine corrente che si sta osservando nel programma.
"""
class modelImagesExiff:
    def __init__(self):
        """
        Costruttore di un oggetto modelImagesExiff: inizializza i due oggetti.
        """
        self._images = ObservableList()
        self._currentImage = ObservableImage()

    def loadImages(self, list):
        """
        Carica i path delle immagini settando la prima immagine in currentImage
        :param list: lista dei path delle immagini .jpg che si vogliono caricare;
        :return: immagine corrente se gli elementi selezionati esistono
        """
        self._images.setElements(list)
        if len(self._images.getElements()) > 0:
            return self.loadCurrentImage()
        else:
            return None

    def loadCurrentImage(self):
        """
        Carica l'immagine corrente
        """
        self._currentImage.loadImage(self._images.getElements()[self._images.getCurrentID()])

    def getLength(self):
        """
        :return: lunghezza della lista di immagini
        """
        return len(self._images.getElements())

    def getCurrentId(self):
        """
        :return: Id dell'immagine corrente
        """
        return self._images.getCurrentID()

    def getCurrentImagePath(self):
        """
        :return: path dell'immagine corrente
        """
        return self._currentImage.getPath()

    def rotateImageOf90(self):
        """
        Ruota l'immagine corrente di 90° in senso orario.
        :return: 
        """
        if self._currentImage.getRotate() == 360 or self._currentImage.getRotate() == 0:
            self._currentImage.setRotate(90)
        else:
            self._currentImage.setRotate(self._currentImage.getRotate() + 90)
        return self._currentImage.getRotate()

    def changeImage(self, op):
        """
        Cambia l'immagine corrente in vase all'operatore op:
        * op = '-' l'immagine corrente viene cambiata impostando quella precedente nella lista
        * op = '+' l'immagine corrente viene cambiata impostando quella successiva nella lista 
        :param op: 
        """
        if op == "-":
            if self._images.getCurrentID() <= 0:
                self._images.setCurrentID(len(self._images.getElements()) - 1)
            else:
                self._images.setCurrentID(self._images.getCurrentID() - 1)
        else:
            if self._images.getCurrentID() >= (len(self._images.getElements()) - 1):
                self._images.setCurrentID(0)
            else:
                self._images.setCurrentID(self._images.getCurrentID() + 1)

        self.loadCurrentImage()

    def getUrlMap(self):
        """
        :return: URL delle mappe
        """
        return self._currentImage.getMapUrl()

    def getRotate(self):
        """
        :return: restituisce la rotazione attuale dell'immagine corrente
        """
        return self._currentImage.getRotate()

    def getExiff(self):
        """
        :return: I tag Exif dell'immagine corrente
        """
        return self._currentImage.getExiff()

    def setRegisterImages(self, slot):
        """
        Consente di Iscriversi ai cambiamenti della lista di immagini.
        :param slot:
        """
        self._images.registerToElements(slot)

    def setRegisterId(self, slot):
        """
        Consente di Iscriversi ai cambiamenti dell'Id dell'immagine corrente.
        :param slot:
        """
        self._images.registerToIdValue(slot)

    def setRegisterRotate(self, slot):
        """
        Consente di iscriversi ai cambiamenti della rotazione dell'immagine corrente.
        :param slot:
        """
        self._currentImage.registerRotate(slot)

    def setRegisterMap(self, slot):
        """
        Consente di Iscriversi ai cambiamenti dei geotag dell'immagine corrente.
        :param slot:
        """
        self._currentImage.registerGeoTag(slot)
