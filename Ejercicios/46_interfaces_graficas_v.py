# -*- coding: utf-8 -*-
from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=600, height=400)
miFrame.pack()

minombre = StringVar()

nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10 )

passLabel = Label(miFrame, text="Contraseña")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10 )

apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="Comentarios")
comentarioLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroComentario = Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=3, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=3, column=2, padx=10, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVert.set)

def codigoBoton():
    minombre.set("JasK")

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()