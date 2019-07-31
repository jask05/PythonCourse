from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Ejercicio Guiado")

# --------------------- Funciones --------------------- 

## Archivo

# Conectar BBDD
def conectarBBDD():
    pass

# Salir del programa
def salirPrograma():
    respuesta = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if respuesta == "yes" or respuesta == True:
        root.destroy()


# ---------------------

# Barra superior
barraMenu = Menu(root)
root.config(menu=barraMenu, width=320, height=420)
# root.config(menu=barraMenu)

miFrame = Frame(root, width=320, height=420)
miFrame.pack()

botonesFrame = Frame(root, width=320, height=420)
botonesFrame.pack()

# Elementos menú
bbddMenu = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.
borrarMenu = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.
crudMenu = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.
ayudaMenu = Menu(barraMenu, tearoff=0) # Principal, a quién pertenece.

# Elementos principales
barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
barraMenu.add_cascade(label="Herramientas", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Elementos hijos Archivo
bbddMenu.add_command(label="Conectar BBDD")
bbddMenu.add_command(label="Salir", command=salirPrograma)

# Elementos hijos Herramientas
borrarMenu.add_command(label="Limpiar campos")

# Elementos hijos CRUD
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

# Elementos hijos Ayuda
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

####### Campos

# ID
idLabel = Label(miFrame, text="ID")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10 )

cuadroID = Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="red", justify="center")

# Nombre
nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
# cuadroNombre.config(fg="red", justify="center")

# Apellido
apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

# Email
emailLabel = Label(miFrame, text="Email")
emailLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroEmail = Entry(miFrame)
cuadroEmail.grid(row=3, column=1, padx=10, pady=10)

# Contraseña
passLabel = Label(miFrame, text="Contraseña")
passLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=4, column=1, padx=10, pady=10)
cuadroPass.config(show="x")

# Botones CRUD
botonCreate = Button(botonesFrame, text="Crear")
botonCreate.grid(row=5, column=0, padx=5, pady=5)
botonCreate = Button(botonesFrame, text="Leer")
botonCreate.grid(row=5, column=1, padx=5, pady=5)
botonCreate = Button(botonesFrame, text="Actualizar")
botonCreate.grid(row=5, column=2, padx=5, pady=5)
botonCreate = Button(botonesFrame, text="Eliminar")
botonCreate.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()