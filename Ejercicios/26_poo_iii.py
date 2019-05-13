# -*- coding: utf-8 -*-

class Coche():
    # Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    # Métodos (Comportamiento)
    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:
            return "Mi coche está en marcha"
        else:
            return "El coche está parado"

    # Estados
    
miCoche = Coche() # Instanciar/ejemplarizar una clase
print("El largo del coche es:",miCoche.largoChasis)
print("El coche tiene:",miCoche.ruedas)
"""
Cuando se instancia, "miCoche" viaja y se instancia en "self" (por parámetro, viaja el propio objeto).
Cuando se pone especifica "self.enmarcha" se traduciría como "miCoche.enmarcha=True"
"""
miCoche.arrancar()
print(miCoche.estado())
