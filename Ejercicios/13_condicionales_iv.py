# -*- coding: utf-8 -*-
print("Programa de becas año 2019")

distancia_escuela = int(input("[+] Introduce la distancia a la escuela en Km: "))
print("Distancia a la escuela: " + str(distancia_escuela) + " kms.")

numero_hermanos = int(input("[+] Número de hermanos: "))
print("Número de hermanos: " + str(numero_hermanos))

salario_familiar = int(input("[+] Salario familiar: "))
print("Salario familiar: " + str(salario_familiar) + " €.")

# if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("[=] Tienes derecho a beca.")
else:
    print("[=] NO tienes derecho a beca.")