from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Ejercicio Guiado")

# --------------------- Funciones --------------------- 

## Archivo

# Conectar BBDD

dbname = "60_ejercicio_guiado_ii.sqlite3"

def conectarBBDD():
	try:
		miConexion = sqlite3.connect(dbname)
		miCursor = miConexion.cursor()
		miCursor.execute('''
				CREATE TABLE DatosUsuarios (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(50),
				apellido VARCHAR(20),
				email VARCHAR(50),
				contrasenia VARCHAR(50),
				comentarios VARCHAR(100))
				''')
	except:
		messagebox.showwarning("Base de datos", "¡La base de datos ya existe!")


# Salir del programa
def salirPrograma():
    respuesta = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if respuesta == "yes" or respuesta == True:
        root.destroy()

# --------------------- CRUD --------------------- 

def createContent():
	miConexion 	= sqlite3.connect(dbname)
	miCursor 	= miConexion.cursor()

	# Re-asignación
	name 	= nombreSV.get()
	surname = apellidoSV.get()
	email 	= emailSV.get()
	passwd 	= passSV.get()
	comment = cuadroComentario.get("1.0", END) # Donde empieza a capturar texto y donde termina

	# Insertar elementos
	miCursor.execute("INSERT INTO DatosUsuarios VALUES(NULL, '" + name + "', '" + surname + "', '" + email + "', '" + passwd + "', '" + comment + "')")
	miConexion.commit()
	# Cerrar conexión
	miConexion.close()

	messagebox.showinfo("Registro", "¡Registro insertado con éxito!")
	cleanContent()

def readContent():
	miConexion 	= sqlite3.connect(dbname)
	miCursor 	= miConexion.cursor()

	# Re-asignación
	idUsuario 	= idSV.get()

	miCursor.execute("SELECT * FROM DatosUsuarios WHERE id=" + idUsuario)
	usuarioBD = miCursor.fetchall()

	if not usuarioBD:
		messagebox.showerror("Error de búsqueda", "El usuario que intenta buscar no existe.")
		cleanContent()
	else:

		for usuario in usuarioBD:
			nombreSV.set(usuario[0])
			apellidoSV.set(usuario[1])
			emailSV.set(usuario[2])
			passSV.set(usuario[3])
			cuadroComentario.insert("1.0", usuario[4])

	miConexion.commit()

def updateContent():
    pass

def deleteContent():
    pass


# Limpia el contenido de los cuadros
def cleanContent():
    idSV.set("")
    nombreSV.set("")
    apellidoSV.set("")
    passSV.set("")
    emailSV.set("")
    cuadroComentario.delete(1.0, END)  
    

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
bbddMenu.add_command(label="Conectar BBDD", command=conectarBBDD)
bbddMenu.add_command(label="Salir", command=salirPrograma)

# Elementos hijos Herramientas
borrarMenu.add_command(label="Limpiar campos", command=cleanContent)

# Elementos hijos CRUD
crudMenu.add_command(label="Crear", command=createContent)
crudMenu.add_command(label="Leer", command=readContent)
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

# Elementos hijos Ayuda
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

####### Campos

# StringVar (solo para los entry)
idSV            = StringVar()
nombreSV        = StringVar()
apellidoSV      = StringVar()
emailSV         = StringVar()
passSV          = StringVar()

# ID
idLabel = Label(miFrame, text="ID")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10 )

cuadroID = Entry(miFrame, textvariable=idSV)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="red", justify="center")

# Nombre
nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=nombreSV)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
# cuadroNombre.config(fg="red", justify="center")

# Apellido
apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroApellido = Entry(miFrame, textvariable=apellidoSV)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

# Email
emailLabel = Label(miFrame, text="Email")
emailLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroEmail = Entry(miFrame, textvariable=emailSV)
cuadroEmail.grid(row=3, column=1, padx=10, pady=10)

# Contraseña
passLabel = Label(miFrame, text="Contraseña")
passLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=passSV)
cuadroPass.grid(row=4, column=1, padx=10, pady=10)
cuadroPass.config(show="x")

# Comentarios
comentarioLabel = Label(miFrame, text="Comentario")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

cuadroComentario = Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=5, column=2, padx=0, pady=10, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVert.set)

# Botones CRUD
botonCreate = Button(botonesFrame, text="Crear", command=createContent)
botonCreate.grid(row=5, column=0, padx=5, pady=5)
botonCreate = Button(botonesFrame, text="Leer", command=readContent)
botonCreate.grid(row=5, column=1, padx=5, pady=5)
botonCreate = Button(botonesFrame, text="Actualizar")
botonCreate.grid(row=5, column=2, padx=5, pady=5)
botonCreate = Button(botonesFrame, text="Eliminar")
botonCreate.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()