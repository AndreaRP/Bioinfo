#coding=utf-8
#Modificar el ejercicio anterior para que elimine los signos de puntuación de las palabras

import string

#Pedimos el nombre del fichero
nombre = raw_input("Nombre del fichero: ")

#apuntamos al fichero
f = open(nombre)

#metemos las lineas en un array
lineas = f.readlines()
# declaramos un nuevo array en el que meteremos las palabras
palabras = []
map = {}

#recorremos cada linea del array, le borramos los retornos de carro (\n) y vamos añadiendo cada palabra a palabras
for linea in lineas:
    linea = linea.strip()
    #sustituimos los signos de puntuación por carácter vacío
    linea = linea.translate(string.maketrans("",""),string.punctuation)
    for palabra in linea.split(' '):
        if palabra not in map.keys():
            map.update({palabra:1})
        else:
            map[palabra]+=1
print map