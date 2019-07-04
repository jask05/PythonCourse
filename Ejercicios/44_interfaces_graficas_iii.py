# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miImagen = PhotoImage(file="/home/jask/Develop/PythonCourse/Ejercicios/Naruto.png")

# miLabel = Label(miFrame, text="Esto es una prueba de Label.")
# Label(miFrame, text="Esto es una prueba de Label.", fg="red", font=("Verdana", 16)).place(x=100, y=200) # Código abreviado
Label(miFrame, image=miImagen).place(x=100, y=200) # Código abreviado
# miLabel.pack() # adapta el contenedor a las dimensiones del label, por eso se queda pequeño.
# miLabel.place(x=100, y=200) # x = borde izquierdo hasta el texto; y = borde superior hasta el texto.

root.mainloop()
