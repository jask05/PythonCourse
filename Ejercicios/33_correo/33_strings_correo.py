# -*- coding: utf-8 -*-

"""
Crea un programa que pida introducir una dirección de email por teclado. El programa
debe imprimir en consola si la dirección de email es correcta o no en función de si esta
tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
o al final, la dirección también será errónea,
"""

def wrongEmail():
    print("[+] El email que has introduce es incorrecto.")

email = input("¿Cuá es tu email?: ")

emailCount = email.count("@")
emailFirstLetter = email[0]
emailLen = len(email)

domains = [".com", ".es", ".org", ".net", ".co.uk", ".com.ar"]

if(emailCount == 1):
    if(emailFirstLetter == "@" or email[emailLen-1] == "@"):
        wrongEmail()
    else:
        if(domains in email):
            print("ok")
        # for domain in domains:
        #     if(email.count(domain)):
        #         print(email.count(domain))
        #         print("[+] Email CORRECTO!!!!")
        #         break
        #     else:
        #         print("[+] Dominio NO encontrado.")
else:
    wrongEmail()

