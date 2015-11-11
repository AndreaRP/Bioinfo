#coding=utf-8
# Realizar un programa que le pida al usuario nombres de ficheros de tipo GenBank, los abra, lea su contenido
# y guarde en otro fichero 'resumen.tst' el nombre del organismo y el número de A de cada fichero. Este fichero puede
# existir previamente y si es así se añaden los datos al final. Si el usuario pulsa como nombre de fichero exit, el programa
# finaliza
n = 0
nombre = raw_input("Nombre de fichero: ")
while nombre != 'exit':
    origen = open(nombre)
    lineas = origen.readlines()
    info = lineas[0].split(" ",1)
    destino = open('resumen.txt','a')
    for linea in lineas[1:]:
        for base in linea:
            if base == 'A':
                n+=1
    destino.write('Descripcion: '+(str(info[1]))+ 'Nº A: '+str(n)+'\n')
    origen.close()
    destino.close()
    nombre = raw_input("Nombre de fichero: ")

