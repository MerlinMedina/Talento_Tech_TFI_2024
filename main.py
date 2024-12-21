from funciones_menu import *  # importa todas las funciones del menú
from funciones_db import (db_crear_tabla_productos,) #importa la función crear tabla de BD

# Declaro la función principal main
def main():
    # Llamo a la función que inicializa la BD y crea la tabla (si no existe)
    db_crear_tabla_productos()

    # Bucle while para mantenerme dentro del menú
    while True:
        # menu_mostrar_opciones() muestra y retorna la opcion seleccionada por el usuario
        opcion = menu()
        limpiar_terminal() # limpia la terminal

        if opcion == "1":
            menu_registrar_producto()
        elif opcion == "2":
            menu_mostrar_productos()
        elif opcion == "3":
            menu_actualizar_producto()
        elif opcion == "4":
            menu_eliminar_producto()
        elif opcion == "5":
            menu_buscar_producto()
        elif opcion == "6":
            menu_reporte_bajo_stock()
        elif opcion == "7": # Opción para salir del bucle while del menú
            print("*" * 45)
            print("*    Usted eligió salir del programa...     *")
            print("\n* Gracias por usar nuestra App, Hasta luego.*")
            print("*" * 45)
            break
        else:
            limpiar_terminal() # limpia la terminal
            print("Opción no válida. Por favor, elija una opción válida.")

        input("Presione enter para continuar") # Pausa para que el usuario pueda ver

main()  # Llamo a la función principal que inicializa el programa
