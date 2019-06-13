# -*- coding: utf-8 -*-

# Utilizando el paquete instalado con pip3
from io import open

# Lectura
archivo_texto = open("37_archivo.txt", "r")
archivo_texto2 = open("37_archivo.txt", "r")

print(archivo_texto.read())

# archivo_texto.seek(10)

print("\n---------------\n")

print(archivo_texto.read())

archivo_texto.seek(20) # los 20 primeros caracteres no los tomará en cuenta.

print("\n---------------\n")

print(archivo_texto.read())

print("\n---------------\n")

print(archivo_texto2.read(5))

# Puntero en medio del archivo

archivo_texto3 = open("37_archivo.txt", "r")

archivo_texto3.seek(len(archivo_texto3.read())/2)
print(archivo_texto3.read())

# Lectura y escritura

archivo_texto_4 = open("38_archivo_rw.txt", "r+")
# print(archivo_texto_4.readlines())
lista_texto = archivo_texto_4.readlines()

lista_texto[1] = "esta línea ha sido modificada desde fuera. \n"

archivo_texto_4.seek(0)
archivo_texto_4.writelines(lista_texto)

archivo_texto.close()
archivo_texto2.close()
archivo_texto3.close()
archivo_texto_4.close()
