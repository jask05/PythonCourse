# -*- coding: utf-8 -*-

class Coche():
    # Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    # Métodos (Comportamiento)
    # También devuelve el estado
    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado."

    def estado(self):
        # if self.enmarcha:
        #     return "Mi coche está en marcha"
        # else:
        #     return "El coche está parado"
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

    # Estados
    
miCoche = Coche() # Instanciar/ejemplarizar una clase
print("El largo del coche es:",miCoche.largoChasis)
print("El coche tiene:",miCoche.ruedas)
"""
Cuando se instancia, "miCoche" viaja y se instancia en "self" (por parámetro, viaja el propio objeto).
Cuando se pone especifica "self.enmarcha" se traduciría como "miCoche.enmarcha=True"
"""
print(miCoche.arrancar(True))
miCoche.estado()

print(" ----------------- Segundo objeto ---------------------")
miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

