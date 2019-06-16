# -*- coding: utf-8 -*-
import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de",self.nombre)

    def __str__(self):
        return "Nombre: {}, Género: {}, Edad: {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas = []

    def __init__(self):
        listaDePersonas = open("41_fichero_externo.txt", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("[+] Se cargaron {} personas del fichero externo.".format(len(self.personas)))
        except:
            print("[+] El fichero está vacío.")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarPersonasFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasFicheroExterno(self):
        listaDePersonas = open("41_fichero_externo.txt", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("[+] La información del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

persona = Persona("Raúl", "Masculino", "29")
miLista.agregarPersona(persona)

# persona = Persona("María", "Femenino", "54")
# miLista.agregarPersona(persona)

# persona = Persona("Santiago", "Masculino", "31")
# miLista.agregarPersona(persona)

miLista.mostrarPersonas()
miLista.mostrarInfoFicheroExterno()