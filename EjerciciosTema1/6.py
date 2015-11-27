# coding=utf-8
# Sabiendo que os.listdir(path) devuelve una lista con todas las entradas del directorio path, abrir todos los ficheros
# con extensión .FASTA que haya en un directorio y guardar en otro fichero 'resumen2.txt' el nombre del organismo y el número de A.
# Este fichero puede existir previamente y si así se añaden los datos al final.

import os


n = 0
files = filter(os.path.isfile, os.listdir(os.curdir))
for file in files:
    if file.split(".")[-1] == 'FASTA':
        origen = open(file)
        lineas = origen.readlines()
        info = lineas[0].split(" ",1)
        destino = open('resumen2.txt','a')
        for linea in lineas[1:]:
            for base in linea:
                if base == 'A':
                    n+=1
        destino.write('Descripcion: '+(str(info[1]))+ 'Nº A: '+str(n)+'\n')
        origen.close()
        destino.close()
