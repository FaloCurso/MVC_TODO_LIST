import sys
import os
# import csv
# Al estar en carpetas distintas a src le damos la ruta con sys.path.append
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.task_controller import (crear_tarea, obtener_todas, actualizar_tarea, obtener_por_id, eliminar_tarea, limpiar_pantalla, buscar_tareas)

def mostrar_menu():
    opcion =""
   
    while True:
        limpiar_pantalla()
        print("\n------ \033[96mMENÚ TAREAS\033[0m -------")
        print("-"*25)
        print("1. Crear tarea")
        print("2. Ver todas las tareas")
        print("3. Ver tarea por ID")
        print("4. Actualizar tarea")
        print("5. Eliminar tarea")
        print("6. Buscar tarea")
        print("7. Salir")
        print("-"*25)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            obtener_todas()
        elif opcion == "3":
            obtener_por_id()
        elif opcion == "4":
            actualizar_tarea()
        elif opcion == "5":
            eliminar_tarea()
        elif opcion == "6":
            buscar_tareas()

        elif opcion == "7":
            print("Gracias, por usar nuestra lista de tareas")
            break
        else:
            print("Opción inválida.")
            input("\n Pulsa intro para continuar")



# def init_tarea():
#     mostrar_menu()

# init_tarea()
