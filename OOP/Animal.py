# coding=utf-8
from abc import abstractmethod

class Animal(object):
    #constructor
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    #Getters y Setters
    def getNombre(self):
        return self.nombre

    def getEspecie(self):
        return self.especie

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEspecie(self, especie):
        self.especie = especie

    #toString
    def __str__(self):
        return "%s es un %s" % (self.nombre, self.especie)

    @abstractmethod
    def hablar(self):
        return


