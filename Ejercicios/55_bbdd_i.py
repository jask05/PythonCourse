import sqlite3

# Abrir-crear conexión
miConexion = sqlite3.connect("55_bbdd_i")

# Crear cursor/puntero
miCursor = miConexion.cursor()

# Ejecuta query
# Solo se tiene que ejecutar una vez porque la tabla "productos" ya existe
# Si se vuelve a ejecutar intentará crear de nuevo la tabla.
# miCursor.execute("CREATE TABLE productos (nombre VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

# Insertar elementos
miCursor.execute("INSERT INTO productos VALUES('Balón', 16, 'Deporte')")

# Verificación y confirmación de cambios
miConexion.commit()

# Cerrar conexión
miConexion.close()