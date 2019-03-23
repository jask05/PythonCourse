tupla = ("Juan", 13, 1, 1955, 45, 5, 78, 13, 9, 13, 4)
tuplaSinPar = "Juan", 13, 1, 1955, 45, 5, 78, 13, 9, 13, 4

print(tupla[:])

# Convierte tupla a lista
lista = list(tupla)
print(lista[:])

# Convierte lista en tupla
tupla2 = tuple(lista)
print(tupla2)

print("# Indice")
indice = tupla.index(13)
print(indice)

print("# Contar elementos se encuentran dentro de una tupla")
contar = tupla.count(13)
print(contar)

print("# Longitud de la tupla")
longitud = len(tupla)
print(longitud)

print("# Tupla unitaria")
tupla = ("elemento", )
print(len(tupla))

# Tupla sin parentesis
print(tuplaSinPar)

print("# Desempaquetado de tupla.")
tupla = ("Juan", 13, 1, 1955)
nombre, dia, mes, anio = tupla
print(nombre)
print(anio)
print(mes)
print(dia)