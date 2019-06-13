# -*- coding: utf-8 -*-
import pickle

fichero = open("39_lista_nombres", "rb")

lista = pickle.load(fichero)

print(lista)