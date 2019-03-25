# -*- coding: utf-8 -*-

# edad = int(input("[+] Introduce una edad mayor que 0 y menor que 100: "))
edad = 50

# Se lee de izquierda a derecha. Si la primera condición es "falsa", pasaría a ejecutar el else. En cambio si es "verdadera" evalua la siguiente condición. Si es falsa, pasa al else, si no, ejecuta la condición.
if 0 < edad < 100:
    print("Edad correcta.")
else:
    print("Edad incorrecta.")

##################################

salario_presidente = int(input("[+] Salario presidente: "))
print("[-] Salario presidente: " + str(salario_presidente) + " €")

salario_director = int(input("[+] Salario director: "))
print("[-] Salario director: " + str(salario_director) + " €")

salario_jefe_area = int(input("[+] Salario jefe de área: "))
print("[-] Salario jefe_area: " + str(salario_jefe_area) + " €")

salario_administrativo = int(input("[+] Salario administrativo: "))
print("[-] Salario administrativo: " + str(salario_administrativo) + " €")

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente.")
else:
    print("Algo falla!")