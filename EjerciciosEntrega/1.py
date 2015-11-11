#coding=utf-8
#Realizar un programa que pida al usuario el nombre de un fichero, lo abra, cuente cuántas palabras
# de cada tipo existen y lo muestre por pantalla

nombre = raw_input("Nombre del fichero: ")
f = open("hola.txt")
g = open("destino.txt","w")
#Abrir fichero de lectura : f = open("fichero.txt")
#Abrir fichero de lectura : f = open("fichero.txt", "r")
#Abrir fichero de lectura en binario : f = open("fichero.txt", "rb")
#Abrir fichero para escribir desde cero : f = open ("fichero.txt", "w")
#Abrir fichero para añadir al final : f = open ("fichero.txt", "a")
for linea in f:
	print(linea)
	g.write(linea)
g.close()
f.close()

#f = open("origen.txt")
#g = open("destino.txt","w")
#linea = f.readline()
#while linea != "":
#  g.write(linea)
#  linea = f.readline()
#g.close()
#f.close()