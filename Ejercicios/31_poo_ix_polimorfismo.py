# -*- coding: utf-8 -*-

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas.")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas.")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas.")

# Polimorfismo
def desplazamientoVehiculos(vehiculo):
    vehiculo.desplazamiento()

# moto = Moto()
# moto.desplazamiento()

# coche = Coche()
# coche.desplazamiento()

# camion = Camion()
# camion.desplazamiento()

miVehiculo = Moto()
desplazamientoVehiculos(miVehiculo)