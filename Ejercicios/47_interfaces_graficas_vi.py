# -*- coding: utf-8 -*-
from tkinter import *

# Calculadora
raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

# ------------------ Pantalla ------------------ #
pantalla = Entry(miFrame)
pantalla.grid(row=1, column=1, pady=2, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# ------------------ Fila 1 ------------------ #
boton7 = Button(miFrame, text="7", width=3)
boton7.grid(row=2, column=1)

boton8 = Button(miFrame, text="8", width=3)
boton8.grid(row=2, column=2)

boton9 = Button(miFrame, text="9", width=3)
boton9.grid(row=2, column=3)

botonD = Button(miFrame, text="/", width=3)
botonD.grid(row=2, column=4)

# ------------------ Fila 2 ------------------ #
boton4 = Button(miFrame, text="4", width=3)
boton4.grid(row=3, column=1)

boton5 = Button(miFrame, text="5", width=3)
boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text="6", width=3)
boton6.grid(row=3, column=3)

botonM = Button(miFrame, text="x", width=3)
botonM.grid(row=3, column=4)

# ------------------ Fila 3 ------------------ #
boton1 = Button(miFrame, text="1", width=3)
boton1.grid(row=4, column=1)

boton2 = Button(miFrame, text="2", width=3)
boton2.grid(row=4, column=2)

boton3 = Button(miFrame, text="3", width=3)
boton3.grid(row=4, column=3)

botonR = Button(miFrame, text="-", width=3)
botonR.grid(row=4, column=4)

# ------------------ Fila 4 ------------------ #
boton0 = Button(miFrame, text="0", width=3)
boton0.grid(row=5, column=1)

botonC = Button(miFrame, text=",", width=3)
botonC.grid(row=5, column=2)

botonI = Button(miFrame, text="=", width=3)
botonI.grid(row=5, column=3)

botonS = Button(miFrame, text="+", width=3)
botonS.grid(row=5, column=4)

raiz.mainloop()