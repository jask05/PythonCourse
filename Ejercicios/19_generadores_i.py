# -*- coding: utf-8 -*-

print("# Función tradicional")
def generarNumerosPares(limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num*2)
        num = num + 1

    return lista

print(generarNumerosPares(10))



print("# Generador")
def generarNumerosPares2(limite):
    num = 1
    while num < limite:
        yield num*2
        num = num + 1

devuelvePares = generarNumerosPares2(12)

# for i in devuelvePares:
    # print(i)

print(next(devuelvePares)) # Devuelve el primer valor almacenado en su interior.
print(" ")
print(next(devuelvePares))
print(" ")
print(next(devuelvePares))