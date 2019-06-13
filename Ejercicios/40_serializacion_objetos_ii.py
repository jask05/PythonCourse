# -*- coding: utf-8 -*-
import pickle

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena)

coche1 = Vehiculos("Ford", "Mustang")
coche2 = Vehiculos("Seat", "León")
coche3 = Vehiculos("Mazda", "CX-5")

coches = [coche1, coche2, coche3]

fichero = open("40_vehiculos", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

# Carga del fichero

ficheroApertura = open("40_vehiculos", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for x in misCoches:
    print(x.estado(), "\n ---------- ")