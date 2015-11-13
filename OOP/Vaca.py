# coding=utf-8
#importo la clase Animal del módulo Animal
from Animal import Animal

class Vaca(Animal):

    especie = 'vaca'

    #constructor
    def __init__(self, nombre, peso):
        super(Vaca,self).__init__(nombre, self.especie)
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def hablar(self):
        print('muuuuuuuuuuuuuuuu')
