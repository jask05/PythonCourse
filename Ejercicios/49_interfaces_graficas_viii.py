# -*- coding: utf-8 -*-
from tkinter import *

# Calculadora
raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""
resultado = 0
contador_resta = 0
contador_multiplicacion = 0
contador_division = 0
num1 = 0

# Mejoras
# - Solo se puede usar una coma.
# - Que se puedan usar números con coma.

# ------------------ Pantalla ------------------ #

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla) # state="readonly"
pantalla.grid(row=1, column=1, pady=2, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# ------------------ Pulsaciones teclado ------------------ #

def numeroPulsado(num):
    global operacion

    if operacion != "":
        numeroPantalla.set(num)
        # operacion = "" # comienza a concatenar de nuevo
    else:
        if numeroPantalla.get() == "0":
            numeroPantalla.set(num)
        else:
            numeroPantalla.set(numeroPantalla.get() + num)

def delNumeros():
    global operacion
    global resultado
    global contador_resta
    global contador_multiplicacion
    global contador_division
    global num1

    operacion = ""
    resultado = 0
    contador_resta = 0
    contador_multiplicacion = 0
    contador_division = 0
    num1 = 0
    numeroPantalla.set(resultado)

def sumar(num):
    global operacion
    global resultado
    
    resultado += int(num)
    operacion = "suma"

    numeroPantalla.set(resultado)

def restar(num):
    global operacion
    global resultado
    global contador_resta
    global num1

    if operacion == "suma":
        num = resultado + int(num)
    elif operacion == "multiplicacion":
        num = resultado * int(num)
    elif operacion == "division":
        num = resultado / int(num)

    if contador_resta == 0:
        num1 = int(num)
        
        if resultado != 0:
            resultado = num1
        else:
            resultado = resultado - num1
    else:
        if contador_resta == 1:
            resultado = int(num1) - int(num)
        else:
            resultado = int(resultado) - int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_resta += 1
    operacion = "resta"

def multiplicar(num):
    global operacion
    global resultado
    global contador_multiplicacion
    global num1

    if contador_multiplicacion == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multiplicacion == 1:
            resultado = int(num1) * int(num)
        else:
            resultado = int(resultado) * int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_multiplicacion += 1
    operacion = "multiplicacion"

def dividir(num):
    global operacion
    global resultado
    global contador_division
    global num1

    if contador_division == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_division == 1:
            resultado = int(num1) / int(num)
        else:
            resultado = int(resultado) / int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_division += 1
    operacion = "division"

def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multiplicacion
    global contador_division
    
    numeroPantallaGet = int(numeroPantalla.get())

    if operacion == "suma":
        numeroPantalla.set(int(resultado) + numeroPantallaGet)
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(int(resultado) - numeroPantallaGet)
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado) * numeroPantallaGet)
        resultado = 0
        contador_multiplicacion = 0
    elif operacion == "division":
        numeroPantalla.set(int(resultado) / numeroPantallaGet)
        resultado = 0
        contador_division = 0

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

botonD = Button(miFrame, text="/", width=3, command=lambda:dividir(numeroPantalla.get()))
botonD.grid(row=3, column=4)

# ------------------ Fila 2 ------------------ #
boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)

botonM = Button(miFrame, text="x", width=3, command=lambda:multiplicar(numeroPantalla.get()))
botonM.grid(row=4, column=4)

# ------------------ Fila 3 ------------------ #
boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)

botonR = Button(miFrame, text="-", width=3, command=lambda:restar(numeroPantalla.get()))
botonR.grid(row=5, column=4)

# ------------------ Fila 4 ------------------ #
botonC = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonC.grid(row=6, column=1)

boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=2)

botonI = Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonI.grid(row=6, column=3)

botonS = Button(miFrame, text="+", width=3, command=lambda:sumar(numeroPantalla.get()))
botonS.grid(row=6, column=4)

# ------------------ Debug ------------------ #
# pantalla2 = Entry(miFrame, textvariable=debugPantalla)
# pantalla2.grid(row=7, column=1, pady=2, columnspan=4)
# pantalla2.config(background="black", fg="#03f943", justify="right")

raiz.mainloop()