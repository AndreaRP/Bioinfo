#coding=utf-8
#en PERL losnombres de variable se forman igual que en Python pero van precedidos del simbolo $.
# Crea un programa que diga si una variable es legal. (Comienza por $, sigue una letra y luego letra o número)

import re

regEx = '\$[a-zA-Z][a-aA-Z0-9]*$'

variable = raw_input("Introduce nombre de var: ")
if re.match(regEx, variable) is not None:
    print('Valida')
else:
    print('Caca')


