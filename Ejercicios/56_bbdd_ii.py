import sqlite3

# Abrir-crear conexión
miConexion = sqlite3.connect("56_bbdd_ii")

# Crear cursor/puntero
miCursor = miConexion.cursor()

# Ejecuta query
# Solo se tiene que ejecutar una vez porque la tabla "productos" ya existe
# Si se vuelve a ejecutar intentará crear de nuevo la tabla.
# miCursor.execute("CREATE TABLE productos (nombre VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

# Insertar elementos
# Listas que contienen tuplas
productos = [ 
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")
]

# miCursor.executemany("INSERT INTO productos VALUES (?,?,?)", productos)

# Leer información
miCursor.execute("SELECT * FROM productos")

rs_miCursor = miCursor.fetchall()

print(rs_miCursor)

# Recorre lista
for producto in rs_miCursor:
    print(producto[0]," => ", producto[1],"€")

# Verificación y confirmación de cambios
miConexion.commit()

# Cerrar conexión
miConexion.close()