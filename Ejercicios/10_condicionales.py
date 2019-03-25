# -*- coding: utf-8 -*-
print("Programa de evaluación de notas de alumnos")

nota_alumno = int(input("Por favor, introduce una nota: "))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(nota_alumno))