# -*- coding: utf-8 -*-
import math

def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas")
        # raise ZeroDivisionError("No se permiten edades negativas")

    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate"

# print(evaluaEdad(-18))

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo.")
    else:
        return math.sqrt(num1)

try:
    print(calculaRaiz(-144))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")