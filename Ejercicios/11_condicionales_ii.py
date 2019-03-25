# -*- coding: utf-8 -*-
print("Verificación de acceso")
edad = int(input("[+] Edad del usuario: "))

if edad < 18:
    print("No puede pasar.")
elif edad > 100:
        print("Edad incorrecta.")
else:
    print("Puede pasar.")

