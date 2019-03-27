# -*- coding: utf-8 -*-

for i in ["Pildoras", "Informáticas", 2019]:
    print("Hola", end="------ \n")

email = False
contador = 0

for i in "hola@micorreo.com":
   if(i == "@" or i == "."):
       contador = contador + 1

if contador >= 2:
    print("[-] Email correcto.")
else:
    print("[-] Email incorrecto.")

for i in range(5):
    print(i)