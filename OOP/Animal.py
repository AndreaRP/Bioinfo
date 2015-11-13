import abc

class Animal(object):
    patas = 0
    nombre = ''

    #constructor
    def __init__(self, patas, nombre):
        self.patas = patas
        self.nombre = nombre


    @abc.abstractmethod
    def hablar(self):
        return

