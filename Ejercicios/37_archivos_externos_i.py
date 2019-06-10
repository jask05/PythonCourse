# -*- coding: utf-8 -*-

# Utilizando el paquete instalado con pip3
from io import open

# Escritura
archivo_texto = open("37_archivo.txt", "w")

frase = "Lorem Ipsum is simply dummy\n text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's\n standard dummy text ever since the 1500s, \n when an unknown printer took a galley\n of type and scrambled it to make a type specimen book."

archivo_texto.write(frase)

archivo_texto.close()

# Lectura
archivo_texto_lectura = open("37_archivo.txt", "r")

texto = archivo_texto_lectura.read()

print(texto)

print("\n ----------------------- \n")

# Lectura en lista
archivo_texto_lectura_2 = open("37_archivo.txt", "r")

texto2 = archivo_texto_lectura_2.readlines()

archivo_texto_lectura_2.close()

print(texto2)
print(texto2[1])

print("\n ----------------------- \n")

# Agregar línea
archivo_texto_append = open("37_archivo.txt", "a")

archivo_texto_append.write("\n Seguimos con el contenido adicionado después.")

archivo_texto_append.close()
