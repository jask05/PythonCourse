# -*- coding: utf-8 -*-
import pickle

lista_nombres = ["Pedro", "Ana", "María", "Raúl"]

fichero_binario = open("39_lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()