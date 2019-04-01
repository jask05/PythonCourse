# -*- coding: utf-8 -*-

""" Crea un programa que pida números infinitamente. Los números introducidos deben
ser cada vez mayores El programa finalizará cuando se introduce un número menor que
el anterior. """

anterior = 0
numero = int(input("[+] Escribe un número: "))

while numero > anterior:
    print("Continúa...")
    anterior = numero
    numero = int(input("[+] Escribe un número: "))

if numero < anterior:
    print(f"[-] El nº introducido \"{numero}\" es menor que el anterior número: \"{anterior}\"")