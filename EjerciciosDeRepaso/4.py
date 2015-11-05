#coding=utf-8
#Escribir un programa que lea una cadena de caracteres que expresan una hora en el formato
#hh:mm:ss y diga si es correcta tanto por número u posición  de los diferentes caracteres
# como por el valor de la hora. En pantalla saldrá el mensaje:
# a) El formato es incorrecto. Cuando haya más de 8 caracteres, o no vayan en bloques de dos números
# o no aparezcan los caracteres.
# b) Los valores no son válidos. Cuando, aunque el formato sea correcto, el valor de las horas,
# minutos o segundos no se válido
# c) Valores válidos, son las hh horas, mm minutos y ss segundos

hora = raw_input("Introduce una hora: ")

def valido (hora):
    partido = hora.split(":")
    print partido
    #comprueba longitud
    if len(hora) == 8:
        print("Formato incorrecto")
    elif len(partido[0])==2 and len(partido[1]==2) and len(partido(2))==2:
        print("Formato incorrecto")
    elif partido[0]<=12 and partido[1] <= 60 and partido[2]<=60:
        print("Correcto")

