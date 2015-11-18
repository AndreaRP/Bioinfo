#coding=utf-8
#Queremos almacenar los artículos que leemos en una BD , pero no nos gusta ninguna de las disponibles, por lo tanto vamos a
#construirla nosotros mismos. La BD será una lista de diccionarios. Cadaa diccionario consta de 5 campos: Título del artículo,
#autores, revista, fecha y nombre del fichero donde guardamos un resúmen del artículo.
#El programa nos permitirá hacer una serie de cosas elegidas por un menú:
# 1. Introducir un nuevo elemento, esto implicará salvarlo en un archivo
# 2. Listar todos los artículos, especificando los 4 primeros campos
# 3. Buscar si existe un artículo dando una palabra clave del artículo
# 4. Buscar si existe un artículo dando el nombre de un autor
# 5. Listar todos los artículos de una determinada revista
# Cada vez que se arranca el programa deberán recuperarse los datos almacenados previamente