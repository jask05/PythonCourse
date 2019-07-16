from tkinter import *

raiz=Tk()
raiz.title("Ejemplo de menú")

# Armando menú
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=200)

# Elementos del menú
archivoMenu = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.
archivoEdicion = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.
archivoHerramientas = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.
archivoAyuda = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.

# Texto de los elementos de menú + elemento al que pertenece
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# Opciones de submenú
# Archivo
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() # Barra separadora
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

# Edición
archivoEdicion.add_command(label="Deshacer")
archivoEdicion.add_command(label="Rehacer")
archivoEdicion.add_separator() # Barra separadora
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


# Ayuda
archivoAyuda.add_command(label="Manual")
archivoAyuda.add_command(label="Versión")


raiz.mainloop()