from tkinter import *

raiz=Tk()
raiz.title("Ejemplo Checkbuttons")

op1 = IntVar()
op2 = IntVar()
op3 = IntVar()

def opcionViaje():
    opcionEscogida = ""
    if op1.get() == 1:
        opcionEscogida += "playa, "
    
    if op2.get() == 1:
        opcionEscogida += "montaña, "
    
    if op3.get() == 1:
        opcionEscogida += "turismo rural"

    textoFinal.config(text=opcionEscogida)

imagen = PhotoImage(file="/home/jask/Develop/PythonCourse/Ejercicios/avion.png")
Label(raiz, image=imagen).pack()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Elige una opción", width=50).pack()

Checkbutton(frame, text="Opción 1", variable=op1, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="Opción 2", variable=op2, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="Opción 3", variable=op3, onvalue=1, offvalue=0, command=opcionViaje).pack()
textoFinal = Label(frame)
textoFinal.pack()

raiz.mainloop()