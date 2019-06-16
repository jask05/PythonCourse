# -*- coding: utf-8 -*-
from tkinter import *

raiz = Tk()

raiz.title("42 - Interfaces gráficas") # Título de la ventana

raiz.resizable(1,1) # Width / height => True/False

raiz.iconbitmap('@icon.xbm')

raiz.geometry("600x300")

raiz.config(bg="#000000")

raiz.mainloop() # Siempre debe ir al final.