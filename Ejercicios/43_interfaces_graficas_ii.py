# -*- coding: utf-8 -*-
from tkinter import *

raiz = Tk()

raiz.title("42 - Interfaces gráficas") # Título de la ventana

# raiz.resizable(1,1) # Width / height => True/False

raiz.iconbitmap('@icon.xbm')

# raiz.geometry("600x300")

raiz.config(bg="#c4c4c4")

miFrame = Frame()

miFrame.pack() # se mete dentro de la raiz

miFrame.config(bg="red")

miFrame.config(width="200",height="300")

# miFrame.pack(expand=1)
miFrame.pack(side="left", anchor="n")
# miFrame.pack(fill="x")
# miFrame.pack(fill="y", expand="True")

miFrame.config(relief="groove")

miFrame.config(bd=20)

miFrame.config(cursor="pirate")

raiz.mainloop() # Siempre debe ir al final.