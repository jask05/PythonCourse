# -*- coding: utf-8 -*-
from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=600, height=400)
miFrame.pack()

nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10 )

passLabel = Label(miFrame, text="Contraseña")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10 )

apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

dirLabel = Label(miFrame, text="Dirección")
dirLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)


raiz.mainloop()