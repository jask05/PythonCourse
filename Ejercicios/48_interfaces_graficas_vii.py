# -*- coding: utf-8 -*-
from tkinter import *

# Calculadora
raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

# ------------------ Pantalla ------------------ #

numeroPantalla = StringVar()
# Debug
debugPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla) # state="readonly"
pantalla.grid(row=1, column=1, pady=2, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# ------------------ Pulsaciones teclado ------------------ #

def numeroPulsado(num):
    getNumPantalla = numeroPantalla.get()
    if num == "0":
        if getNumPantalla != "":
            numeroPantalla.set(getNumPantalla + num)
    else:
        numeroPantalla.set(getNumPantalla + num)
    

def delNumeros():
    numeroPantalla.set("")

def sumar():
    getNumPantalla = numeroPantalla.get()

def restar():
    pass

def multiplicar():
    pass

def dividir():
    pass

def resultado():
    pass

# ------------------ Fila 0 ------------------ #
botonDel = Button(miFrame, text="Delete all", width=24, command=lambda:delNumeros())
botonDel.grid(row=2, column=1, columnspan=4)

# ------------------ Fila 1 ------------------ #
boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)

boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)

botonD = Button(miFrame, text="/", width=3, command=lambda:dividir())
botonD.grid(row=3, column=4)

# ------------------ Fila 2 ------------------ #
boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)

botonM = Button(miFrame, text="x", width=3, command=lambda:multiplicar())
botonM.grid(row=4, column=4)

# ------------------ Fila 3 ------------------ #
boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)

botonR = Button(miFrame, text="-", width=3, command=lambda:restar())
botonR.grid(row=5, column=4)

# ------------------ Fila 4 ------------------ #
botonC = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonC.grid(row=6, column=1)

boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=2)

botonI = Button(miFrame, text="=", width=3, command=lambda:resultado())
botonI.grid(row=6, column=3)

botonS = Button(miFrame, text="+", width=3, command=lambda:sumar())
botonS.grid(row=6, column=4)

# ------------------ Debug ------------------ #
pantalla2 = Entry(miFrame, textvariable=debugPantalla)
pantalla2.grid(row=7, column=1, pady=2, columnspan=4)
pantalla2.config(background="black", fg="#03f943", justify="right")

raiz.mainloop()