from Model.observableObject import *
from PIL import Image
from PIL.ExifTags import *
from Model.localizationUtility import *

"""
La classe ObservableImage rappresenta un'immagine osservabile.

Un'oggetto ObservableImage rappresenterà l'immagine exif, comprendendo la rotazione e i geoTag che saranno due oggetti
osservabili ai quali è possibile iscriversi.
"""
class ObservableImage:
    def __init__(self):
        self._image = None
        self._path = ""
        self._exif = None
        self._mapUrl = ""
        self._geoTag = ObservableObject(False)
        self._rotate = ObservableObject(0)

    def loadImage(self, path):
        """
        Questa funzione avrà il compito di caricare un'immagine. Setta la rotazione a 0 e carica tutti i tag Exiff,
        compresi quelli per la geolocalizzazione.
        :param path: path dell'immagine.
        """
        self._path = path
        self.setRotate(0)
        self._geoTag.value = False
        #Carico tutti i file exiff
        self._image = Image.open(self._path)
        exif_data = self._image._getexif()
        if exif_data != None:
            self._exif = {
                TAGS[k]: v
                for k, v in exif_data.items()
                if k in TAGS
            }

            #imposto i geotag
            geotagging = {}
            for (idx, tag) in TAGS.items():
                if tag == 'GPSInfo':
                    if idx  in exif_data:
                        self._geoTag.value = True
                        for (key, val) in GPSTAGS.items():
                            if key in exif_data[idx]:
                                geotagging[val] = exif_data[idx][key]
                        coord = get_coordinates(geotagging)
                        self._mapUrl = "https://www.google.com/maps/search/?api=1&query=" + str(coord[0]) + "," + str(coord[1])
                    else:
                        self._geoTag.value = False
        else:
            self._image = None
            self._exif = None

    def setImage(self, image):
        """
        :param image:
        """
        self._image = image

    def getImage(self):
        return self._image

    def setPath(self, newVal):
        self._path = newVal

    def getPath(self):
        return self._path

    def setRotate(self, newVal):
            self._rotate.value = newVal

    def getRotate(self):
        return self._rotate.value

    def getExiff(self):
        return self._exif

    def getMapUrl(self):
        return self._mapUrl

    def getGeoTag(self):
        return self._geoTag.value

    def registerRotate(self, slot):
        """
        Permette di iscriversi all'osservabile che rappresenta la rotazione dell'immagine
        :param slot:
        """
        self._rotate.register(slot)

    def registerGeoTag(self, slot):
        """
        Permette di iscriversi all'osservabile che rappresenta la presenza di geotag nell'immagine.
        :param slot:
        """
        self._geoTag.register(slot)