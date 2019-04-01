# -*- coding: utf-8 -*-

""" Crea un programa que pida números positivos indefinidamente. El programa termina
cuando se introduce un número negativo. Finalmente el programa muestras la suma de
todos los números introducidos. """

resultado = 0
numero = int(input("[+] Escribe un número positivo: "))

while numero >= 0:
    print("Continúa...")
    resultado = numero + resultado
    numero = int(input("[+] Escribe otro número positivo: "))

if numero < 0:
    print(f"[-] El nº introducido es negativo. La suma de todos los números positivos es: {resultado}")