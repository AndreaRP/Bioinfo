#coding=utf-8
#Realizar un programa que pida al usuario el nombre de un fichero, lo abra, cuente cuántas palabras
# de cada tipo existen y lo muestre por pantalla

#Pedimos el nombre del fichero
nombre = raw_input("Nombre del fichero: ")

#apuntamos al fichero
f = open(nombre)

#metemos las lineas en un array
lineas = f.readlines()
# declaramos un nuevo array en el que meteremos las palabras
palabras = []

#recorremos cada linea del array, le borramos los retornos de carro (\n) y vamos metiendo las palabras en el array
for linea in lineas:
	linea = linea.strip()
	for palabra in linea.split(' '):
		palabras.append(palabra)

#creamos el diccionario donde guardaremos el numero de palabras
map = {}
for i in palabras:
        if i not in map.keys():
            map.update({i:1})
        else:
            map[i]+=1
print map
