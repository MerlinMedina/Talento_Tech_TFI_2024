from funciones_db import * # Importo todo desde funciones DB
import os # Importo os para limpiar la terminal

# Funcion que muestra el menú
def menu():
    limpiar_terminal()
    print("*" * 18)
    print("* Menú principal *")
    print("*" * 18)
    print(
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input("Ingrese la opción deseada: ")

    # retorno un Str con la opción del menú seleccionada
    return opcion


# Función registrar producto
def menu_registrar_producto():
    print("*" * 22)
    print("* REGISTRAR PRODUCTO *")
    print("*" * 22)
    print("\nIngrese los siguientes datos del producto:")

    # Declaro variable locales por entrada de teclado
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")

    # Ingreso y validacion de la cantidad
    while True:
        try:
            cantidad = int(input("Cantidad: ")) # pruebo que sea un entero
            break
        except Exception as error: # capturo e imprimo el error
            print(f"ERROR cantidad: {error}")

    # Ingreso y validacion del precio
    while True:
        try:
            precio = float(input("Precio: ")) # pruebo que sea un flotante
            break
        except Exception as error: # capturo e imprimo el error
            print(f"ERROR precio: {error}")

    # Paso las variables locales en argumentos de la función insertar producto. 
    # El valor que retorna la función insertar producto lo guardo en una variable
    # local booleana llamada resultado para verificar si se insertó correctamente.
    resultado = db_insertar_producto(nombre, descripcion, categoria, cantidad, precio)
    if resultado == True:
        limpiar_terminal()
        print("*" * 37)
        print("* ¡Registro insertado exitosamente! *")
        print("*" * 37)
        print(f"\n|Nombre: {nombre}|Descripción: {descripcion}|Categoria: {categoria}|Cantidad: {cantidad}|Precio: {precio}|\n")
    else:
        print("Algo fallo")


# Función mostrar productos
def menu_mostrar_productos():
    print("*" * 20)
    print("* MOSTRAR PRODUCTO *")
    print("*" * 20)

    lista_productos = db_get_productos()  # llama a la funcion que retorna una lista de tuplas con el contenido de la tabla

    if not lista_productos:
        print("\nNo hay productos que mostrar")
    else:
        for producto in lista_productos: # itero los elementos de la lista y lo imprimo
            print(producto)


""""
def menu_actualizar_producto()

1. solicita al usuario que ingrese el id del producto a modificar
2. busca el producto en la tabla (si no existe informamos)
3. muestra la cantidad actual y solicita que ingrese la nueva cantidad
4. llama a db_actualizar_registro(id, nueva_cantidad) para que actualice la cantidad

"""

# Función actualizar producto
def menu_actualizar_producto():
    print("*" * 23)
    print("* ACTUALIZAR PRODUCTO *")
    print("*" * 23)

    while True: # bucle while hasta que ponga un entero
        try: # pruebo que sea un entero
            id = int(input("Ingrese el id del producto a actualizar: ")) # pido un etero por ingreso de teclado y lo almaceno en una variable
            break
        except Exception as error: # capturo e imprimo el error
            print(f"ERROR id: {error}")

    # id = int(input("Ingrese el id del producto a actualizar: ")) # pido un etero por ingreso de teclado y lo almaceno en una variable
    producto = db_get_producto_by_id(id) # le envio la variable id por argumento de la funcion get producto y almaceno la lista que devuelve en una variable
    if producto: # si devuelve una lista imprimo el producto y actualizo la cantidad
        print(producto)
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        db_actualizar_producto(id, nueva_cantidad)
        limpiar_terminal()
        print("*" * 39)
        print("* ¡Cantidad actualizada exitosamente! *")
        print("*" * 39)

    else: # si devuelve una lista vacia
        print("No existe el producto con el id ingresado")


# Función eliminar producto
def menu_eliminar_producto():
    print("*" * 21)
    print("* ELIMINAR PRODUCTO *")
    print("*" * 21)

    id = int(input("Ingrese el id del producto a eliminar: ")) # pide un entero y lo guarda en uuna variable
    producto = db_get_producto_by_id(id) # # envío la variable id por argumento de la función get producto y almaceno la lista que devuelve en una variable
    if producto: # si devuelve una lista imprimo el producto y lo elimino
        limpiar_terminal()
        print(producto)
        db_eliminar_producto(id)
        print("*" * 37)
        print("* ¡Producto eliminado exitosamente! *")
        print("*" * 37)

    else: # si devuelve una lista vacia
        print("No existe el producto con el id ingresado")


# función buscar producto
def menu_buscar_producto():
    print("*" * 19)
    print("* BUSCAR PRODUCTO *")
    print("*" * 19)

    id = int(input("Ingrese el id a buscar: ")) # pido un etero por ingreso de teclado y lo almaceno en una variable
    producto = db_get_producto_by_id(id)

    if not producto:
        print("No se ha encontrado el producto")
    else:
        print(producto)


# Función reporte de bajo stock
def menu_reporte_bajo_stock():
    print("*" * 25)
    print("* REPORTE DE BAJO STOCK *")
    print("*" * 25)

    minimo_stock = int(
        input("Ingrese el número minimo de stock, luego presione enter: ")
    )
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos con stock menor a : " + str(minimo_stock))

# Función para limpiar la terminal, para mejorar la UX/UI
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
