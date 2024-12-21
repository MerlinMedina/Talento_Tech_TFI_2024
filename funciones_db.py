import sqlite3 # Importo la librería para ejecutar sqlite3

# Declaro las constantes
ruta = r"E:\Merlin\Python\entrega final\inventario.db" # ruta donde se encuentra el archivo de la base de datos


# Función para conectar la base de datos
def conectar_db():
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor() 
    return conexion, cursor


"""
db_crear_tabla_productos()

Esta función utiliza sqlite3 para crear/conectarse con la base "inventario.db" y crea la tabla productos
"""

# Función para crear una tabla de datos si no existe. en caso de que exista se conecta con ella.
# en la query especificamos la PK y definimos los nombres de las columnas
def db_crear_tabla_productos():
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor()
    cursor.execute(
        """ 
CREATE TABLE IF NOT EXISTS productos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
descripcion TEXT,
categoria TEXT NOT NULL,
cantidad INTEGER NOT NULL,
precio REAL NOT NULL
)
"""
    )
    conexion.commit() # confirmamos los cambios realizados
    conexion.close() # cerramos la conexion


"""
db_insertar_producto(producto)

1. recibe como argumento un diccionario con las clave/valor de cada campo de la tabla
2. inserta los datos en la tabla productos
"""

# Función insertar producto
def db_insertar_producto(nombre, descripcion, categoria, cantidad, precio): # recive como argumento el valor de cada campo de la table

    try:
        conexion, cursor = conectar_db()
        query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)"
        placeholder = (precio, descripcion, categoria, cantidad, nombre)
        cursor.execute(query, placeholder)
        conexion.commit()
        state = True
    except Exception as error:
        print(f"Error: {error}")
        conexion.close()
        state = False
    finally:
        conexion.close()
        return state


# Función get productos
def db_get_productos():
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor()  
    query = "SELECT * FROM productos" # lee todos los datos de la tabla productos
    cursor.execute(query)
    lista_productos = cursor.fetchall()  # retorna una lista de tuplas
    conexion.close()
    return lista_productos


# Función get productos by id
def db_get_producto_by_id(id):
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor() 
    query = "SELECT * FROM productos WHERE id = ?" # lee solo los datos del numero de id que trae como argumento
    placeholders = (id,)
    cursor.execute(query, placeholders)
    producto = cursor.fetchone()  # retorna una tupla
    conexion.close()
    return producto


# Función actualizar producto
def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor()  
    query = "UPDATE productos SET cantidad = ? WHERE id = ?" # actualiza la cantidad de producto del id, amos los trae por argumento
    placeholders = (nueva_cantidad, id)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


# Función eliminar
def db_eliminar_producto(id):
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor()  
    query = "DELETE FROM productos WHERE id = ?" # borramos unicamento el producto con el id que trae por argumento
    placeholders = (id,)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()
    

# Función get productos by condicion
def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor() 
    query = "SELECT * FROM productos WHERE cantidad < ?" # lee los productos que cumplen con la condición < que el argumento
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall()  # retorna una lista de tuplas
    conexion.close()
    return lista_productos
