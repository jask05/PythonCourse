# -*- coding: utf-8 -*-
print("Asignaturas optativas año 2019.")
print("[-] Listado de asignaturas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("[+] Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("[-] Asignatura escogida: " + asignatura)
else:
    print("[-] La asignatura escogida no está en la lista.")