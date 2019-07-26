import sqlite3

# Abrir-crear conexión
miConexion = sqlite3.connect("57_bbdd_iii.sqlite3")

# Crear cursor/puntero
miCursor = miConexion.cursor()

# Ejecuta query
# Solo se tiene que ejecutar una vez porque la tabla "productos" ya existe
# Si se vuelve a ejecutar intentará crear de nuevo la tabla.
# Los ''' sirve para dividir la consulta en varios renglones.
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS (
#     codigo_articulo VARCHAR(4) PRIMARY KEY,
#     nombre_articulo VARCHAR(50),
#     precio INTEGER,
#     seccion VARCHAR(20))
# ''')

# Primary key autoincremental
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_articulo VARCHAR(50),
    precio INTEGER,
    seccion VARCHAR(20))
''')

# Contenido de la BD
productos = [
    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica")
]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

# ID autoincrement
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 28, 'juguetería')")

# Verificación y confirmación de cambios
miConexion.commit()

# Cerrar conexión
miConexion.close()