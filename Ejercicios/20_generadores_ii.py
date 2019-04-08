# -*- coding: utf-8 -*-

# Cuando se coloca un asterisco se indica que recibe nº
# indeterminado de elementos y también se le indica
# que estos argumentos serán tuplas
# Yield from simplifica la siguiente sintáxis
"""
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
"""

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Valencia", "Bilbao")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))