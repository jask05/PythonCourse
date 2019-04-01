# -*- coding: utf-8 -*-

# Continue
for letra in "Python":

    if letra == "h" or letra == "n":
        continue

    print("Viendo la letra " + letra)


nombre = "hola hola"
contador = 0

for i in nombre:
    if i == " ":
        continue
    
    contador+= 1

print(contador)

# Pass
class Miclase:
    pass

# Else
email = input("[-] Introduce tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(arroba)