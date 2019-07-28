import sqlite3

# Abrir-crear conexión
miConexion = sqlite3.connect("58_bbdd_iv.sqlite3")

# Crear cursor/puntero
miCursor = miConexion.cursor()

# Ejecuta query
# Solo se tiene que ejecutar una vez porque la tabla "productos" ya existe
# Si se vuelve a ejecutar intentará crear de nuevo la tabla.
# Los ''' sirve para dividir la consulta en varios renglones.
# Primary key autoincremental
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre_articulo VARCHAR(50) UNIQUE,
#     precio INTEGER,
#     seccion VARCHAR(20))
# ''')

# Contenido de la BD
productos = [
    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("destornilladores", 35, "ferretería"),
    ("jarrón", 45, "cerámica")
]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

# ID autoincrement
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



# CRUD
# Create
# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 28, 'juguetería')")

# Read
miCursor.execute("SELECT * FROM productos WHERE seccion='ferretería'")
productos = miCursor.fetchall()
print(productos)

# Update
miCursor.execute("UPDATE productos SET precio='2' WHERE id=1")

# Delete
miCursor.execute("DELETE FROM productos WHERE id=4")

# Verificación y confirmación de cambios
miConexion.commit()

# Cerrar conexión
miConexion.close()