#coding=utf-8
#Modificar el ejercicio anterior para que muestre sólo las cien palabras más frecuentes ordenadas por número de aparición

import string
import operator

# declaramos un nuevo array en el que meteremos las palabras
palabras = []
map = {}
#Pedimos el nombre del fichero
nombre = raw_input("Nombre del fichero: ")

#apuntamos al fichero
f = open(nombre)

#metemos las lineas en un array
lineas = f.readlines()

#recorremos cada linea del array, le borramos los retornos de carro (\n) y vamos añadiendo cada base a palabras
for linea in lineas:
    linea = linea.strip()
    #sustituimos los signos de puntuación por carácter vacío
    linea = linea.translate(string.maketrans("",""),string.punctuation)
    for palabra in linea.split(' '):
        if palabra not in map.keys():
            map.update({palabra:1})
        else:
            map[palabra]+=1

f.close()

map = sorted(map.items(), key=operator.itemgetter(1))[:100]
print(map)
