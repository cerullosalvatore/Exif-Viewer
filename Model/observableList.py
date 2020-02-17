from Model.observableObject import *
"""
La classe ObservableList rappresenta una lista osservabile.

Un oggetto di questa classe avrà due oggetti:
* _elements: E' un oggetto osservabile di tipo lista.
* _currentID: E' un oggetto osservabile di tipo int che rappresenterà l'id corrente  nella lista.
"""
class ObservableList:
    def __init__(self):
        self._elements = ObservableObject([])
        self._currentID = ObservableObject(0)

    def setElements(self, list):
        """
        Imposto gli elementi all'interno dell'elemento osservabile di tipo lista
        :param list: lista
        """
        self.setCurrentID(0)
        self._elements.value = list.copy()

    def getElements(self):
        """
        :return: la lista
        """
        return self._elements.value

    def setCurrentID(self, newVal):
        """
        Cambia il valore dell'id corrente
        :param newVal:
        """
        self._currentID.value = newVal

    def getCurrentID(self):
        return self._currentID.value

    def incrementCurrentId(self):
        """
        Incremeneta di 1 il valore dell'Id corrente
        """
        if self._currentID.value >= (len(self._images.value)-1):
            self._currentID.value = 0
        else:
            self._currentID.value = self._currentID.value + 1

    def decrementCurrentId(self):
        """
        Decrementa di 1 il valore dell'Id corrente.
        """
        if self._currentID.value <= 0:
            self._currentID.value = len(self._images.value)-1
        else:
            self._currentID.value = self._currentID.value -1

    def registerToElements(self, slot):
        """
        Permette di iscriversi ai cambiamenti dell'oggetto _elements che rappresenta la lista osservabile
        :param slot:
        """
        self._elements.register(slot)

    def registerToIdValue(self, slot):
        """
        Permette si iscriversi ai cambiamenti dei valori dell'Id del sistema.
        :param slot:
        """
        self._currentID.register(slot)
