diccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Espania":"Madrid"}

print(diccionario["Francia"])
print(diccionario)

diccionario["Italia"]="Lisboa"
print(diccionario)

diccionario["Italia"]="Roma"
print(diccionario)

del diccionario["Reino Unido"]
print(diccionario)

diccionario = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(diccionario)

tupla = ["Spain", "France", "United Kingdom", "Germany"]
diccionario = {tupla[0]:"Madrid", tupla[1]:"Paris", tupla[2]:"Londres", tupla[3]:"Berlin"}
print(diccionario)
print(diccionario["France"])

diccionario = { 23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionario)
print(diccionario["anillos"])
print(diccionario["anillos"][2])

diccionario = { 23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(diccionario["anillos"])
print(diccionario["anillos"]["temporadas"])
print(diccionario["anillos"]["temporadas"][2])

print("# Imprime las claves: ")
print(diccionario.keys())
print("# Imprime los valores: ")
print(diccionario.values())
print("# Devuelve la longitud del diccionario: ")
print(len(diccionario))