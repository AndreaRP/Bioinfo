# coding=utf-8
import Animal
import Vaca

nuevoAnimal = Animal.Animal('Pelusa','Hamster')
nuevaVaca = Vaca.Vaca('Daisy',120)

print(nuevoAnimal.__str__())
print(nuevaVaca.__str__())
print(nuevaVaca.getNombre() + ' dice'),
nuevaVaca.hablar()