#coding=utf-8
# Pedir al usuario una cadena de adn y contar cuántas veces aparece cada una de las bases.
# Hacer que esto se repita en un bucle infinito.
while True:
    cadena=raw_input("Introduce cadena: ")
    map={}
    for i in cadena:
        if i not in map.keys():
            map.update({i:1})
        else:
            map[i]+=1
    print map