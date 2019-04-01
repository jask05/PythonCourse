# -*- coding: utf-8 -*-

for i in range(5,40,3):
    print(f"Valor de la variable: {i}")

strjask = "jask.zemula@gmail.com"
lenjask = len(strjask)
for i in range(lenjask):
    print(f"Repetición: {i}")

valido = False
email = input("Introduce tu email: ")
for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto!!")
else:
    print("Email incorrecto.")