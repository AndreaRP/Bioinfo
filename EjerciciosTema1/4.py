#coding=utf-8
#Realizar un programa que pida el nombre de un fichero al usuario, lo lea y
# cree otro fichero con el mismo contenido pero con las lineas invertidas
lineas = []
nombre = raw_input("Nombre de fichero: ")
origen = open(nombre)
destino = open("destino","w")
lineas = origen.readlines()
lineas.reverse()
for linea in lineas:
	linea = linea.strip()
	destino.write(linea+'\n')

origen.close()
destino.close()