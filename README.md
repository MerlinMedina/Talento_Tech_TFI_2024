# TALENTO TECH 2024 PROGRAMACIÓN INICIAL PYTHON

# Proyecto Final Integrador. Gestión de Productos en Python.

Este proyecto en Python es una aplicación de consola para gestionar un inventario de productos. Permite realizar operaciones básicas sobre los productos, tales como registrar, mostrar, actualizar, eliminar, buscar y generar reportes de bajo stock, utilizando una base de datos SQLite para almacenar la información.

## Funcionalidades

El programa cuenta con un menú interactivo que permite al usuario realizar las siguientes operaciones:

1. **Agregar producto**: Permite ingresar nuevos productos al inventario, especificando nombre, descripción, categoría, cantidad y precio.
2. **Mostrar productos**: Muestra todos los productos registrados en la base de datos.
3. **Actualizar producto**: Permite modificar la cantidad de un producto existente.
4. **Eliminar producto**: Permite eliminar un producto del inventario por su ID.
5. **Buscar producto**: Permite buscar un producto por su ID y mostrar sus detalles.
6. **Reporte bajo stock**: Muestra una lista de productos cuyo stock es inferior al mínimo especificado por el usuario.
7. **Salir**: Termina la ejecución del programa.

## Estructura del Proyecto

El proyecto está compuesto por tres archivos principales:

### 1. `main.py`

Este archivo contiene la función principal del programa, que inicializa la base de datos y gestiona el menú interactivo. El programa se ejecuta a partir de esta función, mostrando el menú y esperando la entrada del usuario.

### 2. `funciones_menu.py`

Este archivo define las funciones que gestionan la interacción con el usuario. Estas funciones incluyen la presentación del menú y la captura de entradas para las diferentes operaciones:

- **`menu()`**: Muestra el menú principal con las opciones disponibles.
- **`menu_registrar_producto()`**: Solicita al usuario los detalles de un nuevo producto y lo registra en la base de datos.
- **`menu_mostrar_productos()`**: Muestra todos los productos registrados en la base de datos.
- **`menu_actualizar_producto()`**: Permite al usuario actualizar la cantidad de un producto existente.
- **`menu_eliminar_producto()`**: Permite eliminar un producto de la base de datos, dado su ID.
- **`menu_buscar_producto()`**: Permite buscar un producto por su ID y ver sus detalles.
- **`menu_reporte_bajo_stock()`**: Muestra los productos con stock inferior al valor ingresado por el usuario.
- **`limpiar_terminal()`**: Limpia la pantalla de la terminal para mejorar la experiencia de usuario.

### 3. `funciones_db.py`

Este archivo define las funciones necesarias para interactuar con la base de datos SQLite. Las funciones incluyen la creación de la tabla de productos, inserción de productos, actualización, eliminación y consultas. Aquí están las funciones clave:

- **`conectar_db()`**: Establece la conexión con la base de datos SQLite y devuelve el objeto de conexión y el cursor.
- **`db_crear_tabla_productos()`**: Crea la tabla `productos` en la base de datos si no existe.
- **`db_insertar_producto(nombre, descripcion, categoria, cantidad, precio)`**: Inserta un nuevo producto en la base de datos.
- **`db_get_productos()`**: Obtiene todos los productos registrados en la base de datos.
- **`db_get_producto_by_id(id)`**: Busca un producto por su ID y devuelve sus detalles.
- **`db_actualizar_producto(id, nueva_cantidad)`**: Actualiza la cantidad de un producto dado su ID.
- **`db_eliminar_producto(id)`**: Elimina un producto de la base de datos dado su ID.
- **`db_get_productos_by_condicion(minimo_stock)`**: Obtiene productos cuyo stock es inferior al valor especificado.

## Requisitos

Este proyecto requiere Python 3.x y una base de datos SQLite. No es necesario instalar dependencias adicionales, ya que SQLite está integrado en Python.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/usuario/mi-proyecto.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd mi-proyecto
   ```

3. Ejecuta el programa:

   ```bash
   python main.py
   ```

El programa iniciará y mostrará el menú interactivo en la terminal.

## Ejemplos de Uso

- **Agregar producto**: Si seleccionas la opción 1, se te pedirá ingresar el nombre, descripción, categoría, cantidad y precio del producto. El producto se registrará en la base de datos.
  
  Ejemplo:
  ```
  Nombre: Teclado
  Descripción: Teclado mecánico
  Categoría: Computación
  Cantidad: 10
  Precio: 50.00
  ```

- **Mostrar productos**: La opción 2 te mostrará una lista de todos los productos registrados en la base de datos.

- **Actualizar producto**: Si eliges la opción 3, podrás ingresar el ID de un producto y modificar su cantidad. La base de datos se actualizará con la nueva cantidad.

  Ejemplo:
  ```
  ID del producto: 3
  Nueva cantidad: 15
  ```

- **Eliminar producto**: La opción 4 te permitirá eliminar un producto de la base de datos, solicitando su ID.

  Ejemplo:
  ```
  ID del producto a eliminar: 3
  ```

- **Buscar producto**: Si eliges la opción 5, podrás buscar un producto por su ID y visualizar sus detalles.

  Ejemplo:
  ```
  ID del producto a buscar: 3
  ```

- **Reporte bajo stock**: La opción 6 te pedirá ingresar un número mínimo de stock y mostrará los productos cuyo stock es inferior a ese valor.

  Ejemplo:
  ```
  Número mínimo de stock: 5
  ```

## Contribuciones

Si deseas contribuir al proyecto, por favor abre un *pull request* con las mejoras o correcciones que hayas realizado. Asegúrate de seguir las buenas prácticas de programación y de probar el código antes de enviarlo.

---

Con esto, el `README.md` ahora incluye toda la información relevante sobre el proyecto, sus funcionalidades y cómo interactúa con la base de datos. Esto debería ser útil para cualquier persona que desee entender el flujo del programa o colaborar en él. Si necesitas algún ajuste adicional, ¡déjame saber!
