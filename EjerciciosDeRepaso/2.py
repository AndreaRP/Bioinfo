#coding=utf-8
#Escribir un programa que pida al usuario el número del que se quiere calcular el factorial
numero = int(raw_input("Introduce el número: "))


def factorialRecursivo(i):
    if i == 0:
         f = 1
    else:
         f = i * factorialRecursivo(i-1)
    return f

def factorialNoRecursivo(i):
    f = 1
    while (i > 0):
        f = f * i
        i = i - 1
    return f

print(factorialRecursivo(numero))
print(factorialNoRecursivo(numero))