# -*- coding: utf-8 -*-

i = 1
while i <= 10:
    print(f"Iteración número: {i}")
    print("Iteración nº " + str(i))
    i = i + 1

edad = int(input("¿Cuál es tu edad? "))

while edad <= 0 or edad >= 100:
    print("La edad que has introducido es incorrecta.")
    edad = int(input("¿Cuál es tu edad? "))


print("[-] Programa de cálculo de raíz cuadrada.")
numero = int(input("[+] Introduce un número, por favor: "))
intentos = 0
while numero < 0:
    print("[-] No se puede hallar la raíz cuadrada de un número negativo.")

    if intentos == 2:
        print("[-] Has consumido demasiados intentos. El programa ha finalizado")
        break;

    numero = int(input("[+] Introduce un número, por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {solucion}")