from tkinter import *

raiz=Tk()

def imprimir():
    # print(varOpcion.get())
    varOpcionGet = varOpcion.get()
    if varOpcionGet == 1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcionGet == 2:
        etiqueta.config(text="Has elegido femenino")
    elif varOpcionGet == 3:
        etiqueta.config(text="Has elegido otros")

varOpcion = IntVar()
Label(raiz, text="Género: ").pack()

Radiobutton(raiz, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(raiz, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()