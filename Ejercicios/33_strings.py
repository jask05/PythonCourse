# -*- coding: utf-8 -*-

nombreUsuario = input("[+] Introduce el nombre de usuario: ")

print("El nombre es:",nombreUsuario)
print("El nombre es:",nombreUsuario.upper())
print("El nombre es:",nombreUsuario.capitalize())
print("El nombre es:",nombreUsuario.isdigit())
print("El nombre es:",nombreUsuario.isalpha())

edad = input("[+] Introduce la edad: ")
# print("¿Es un dígito? =>",edad.isdigit())

while edad.isdigit() == False:
    
    print("[-] Por favor, introduce un valor numérico.")
    edad = input("[+] Introduce la edad: ")

if(int(edad) < 18):
    print("NO puede pasar")
else:
    print("Puede pasar")