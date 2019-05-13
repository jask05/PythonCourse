# -*- coding: utf-8 -*-

class Coche():

    # Constructor
    def __init__(self):

        # Propiedades
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # encapsulada
        self.__enmarcha = False # Solo se puede cambiar llamando al método arrancar
    
    # Métodos (Comportamiento)
    # También devuelve el estado
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo() # esta variable solo se usa en el método "arrancar"

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chqueo. No podemos arrancar"
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeo(self):
        print("[-] Realizando chequeo interno... ")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

print(" ------------- MiCoche ---------------")    
miCoche = Coche() # Instanciar/ejemplarizar una clase
print(miCoche.arrancar(True))
miCoche.estado()
# print(miCoche.chequeo()) # no tiene sentido

print(" ------------- MiCoche2 ---------------")
miCoche2 = Coche() # Instanciar/ejemplarizar una clase
print(miCoche2.arrancar(False))
miCoche2.estado()
