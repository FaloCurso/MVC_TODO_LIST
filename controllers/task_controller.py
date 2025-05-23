import sys
import os
from sqlalchemy import or_
from database.db import SessionLocal
from models.task_model import Tarea

# Colores ANSI
COLOR_CIERRE = "\033[0m"
COLOR_VERDE = "\033[92m"
COLOR_CYAN = "\033[96m"
COLOR_ROJO = "\033[91m"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tarea():
    limpiar_pantalla()
    try:
        print(f"\n------------------ {COLOR_CYAN}\033[1mCrear Tarea{COLOR_CIERRE} ------------------\n")
        titulo = input(f"{COLOR_CYAN}{'Título:':<15}{COLOR_CIERRE}")

        if len(titulo) > 100:
            raise ValueError(f"{COLOR_ROJO}Título demasiado largo, máximo 100{COLOR_CIERRE}")
        if not titulo.strip():
            raise ValueError(f"{COLOR_ROJO}Título está vacío{COLOR_CIERRE}")
        
        descripcion = input(f"{COLOR_CYAN}{'Descripción:':<15}{COLOR_CIERRE}")

        if len(descripcion) > 500:
            raise ValueError(f"{COLOR_ROJO}Descripción demasiado larga, máximo 500{COLOR_CIERRE}")
        if not descripcion.strip():
            raise ValueError(f"{COLOR_ROJO}La descripción está vacía{COLOR_CIERRE}")
        
        db = SessionLocal()
        nueva = Tarea(titulo=titulo, descripcion=descripcion)
        db.add(nueva)
        db.commit()
        db.close()
        input(f"\n{COLOR_VERDE}Tarea grabada correctamente, pulsa intro para continuar{COLOR_CIERRE}")

    except ValueError as e:
        print(f"{COLOR_ROJO}Error {e}{COLOR_CIERRE}")
        input(f"\n{COLOR_VERDE}Pulsa intro para continuar...{COLOR_CIERRE}")
    except Exception as e:
        print(f"{COLOR_ROJO}Ocurrió un error al procesar los datos: {e}{COLOR_CIERRE}")
        input(f"\n{COLOR_VERDE}Pulsa intro para continuar...{COLOR_CIERRE}")

def obtener_todas():
    limpiar_pantalla()
    db = SessionLocal()
    try:
        tareas = db.query(Tarea).all()
        if not tareas:
            print(f"{COLOR_ROJO}No hay tareas registradas.{COLOR_CIERRE}")
            return

        tareas_ordenadas = sorted(tareas, key=lambda t: (t.estado, t.id_tarea))
        print("-" * 115)
        print(f"{COLOR_CYAN}{'Id':<3} {'Título':<40} {'Descripción':<60} {'Estado':<10}{COLOR_CIERRE}")
        print("-" * 115)
        for t in tareas_ordenadas:
            estado = 'EN CURSO' if t.estado == 1 else 'FINALIZADA'
            if t.estado == 1:
                print(f"{t.id_tarea:>3} {t.titulo:<40} {t.descripcion:<60} {estado:<10}")
            else:
                print(f"\033[35m{t.id_tarea:>3} {t.titulo:<40} {t.descripcion:<60} {estado:<10}\033[0m")
                

    except Exception as e:
        print(f"{COLOR_ROJO}Error al obtener la lista de tareas: {e}{COLOR_CIERRE}")
    finally:
        db.close()
        input(f"\n{COLOR_VERDE}Pulsa intro para continuar...{COLOR_CIERRE}")

def obtener_por_id():
    limpiar_pantalla()
    id_tarea = pedir_id()
    db = SessionLocal()
    tarea = db.query(Tarea).filter(Tarea.id_tarea == id_tarea).first()
    if tarea:
        mostrar_tarea(tarea, "Mostrar Tarea")
    else:
        print(f"{COLOR_ROJO}Tarea no encontrada.{COLOR_CIERRE}")
    db.close()
    input(f"\n{COLOR_VERDE}Pulsa intro para continuar{COLOR_CIERRE}")

def actualizar_tarea():
    limpiar_pantalla()
    id_tarea = pedir_id()
    db = SessionLocal()
    try:
        tarea = db.query(Tarea).filter(Tarea.id_tarea == id_tarea).first()
        if not tarea:
            print(f"{COLOR_ROJO}Tarea no encontrada.{COLOR_CIERRE}")
            return

        mostrar_tarea(tarea, "Actualizar Tarea")
        print(f"Deja {COLOR_VERDE}vacío{COLOR_CIERRE} y pulsa {COLOR_VERDE}intro{COLOR_CIERRE} para {COLOR_VERDE}NO cambiar el valor actual{COLOR_CIERRE}")
        print("---------------------------------------------------------------------------")

        while True:
            nuevo_titulo = input(f"{COLOR_CYAN}Título{COLOR_CIERRE} [{tarea.titulo}]: ") or tarea.titulo
            if len(nuevo_titulo) <= 100:
                break
            print(f"{COLOR_ROJO}El título no puede tener más de 100 caracteres.{COLOR_CIERRE}")

        while True:
            nueva_descripcion = input(f"{COLOR_CYAN}Descripción{COLOR_CIERRE} [{tarea.descripcion}]: ") or tarea.descripcion
            if len(nueva_descripcion) <= 500:
                break
            print(f"{COLOR_ROJO}La descripción no puede tener más de 500 caracteres.{COLOR_CIERRE}")

        estado_actual = "1" if tarea.estado == 1 else "0"
        while True:
            nuevo_estado_input = input(f"{COLOR_CYAN}Estado{COLOR_CIERRE} (1 = EN CURSO, 0 = FINALIZADA) [{estado_actual}]: ") or estado_actual
            try:
                nuevo_estado = int(nuevo_estado_input)
                if nuevo_estado in [0, 1]:
                    break
                print(f"{COLOR_ROJO}El estado solo puede ser 1 (EN CURSO) o 0 (FINALIZADA).{COLOR_CIERRE}")
            except ValueError:
                print(f"{COLOR_ROJO}El estado debe ser un número entero (0 o 1).{COLOR_CIERRE}")

        tarea.titulo = nuevo_titulo
        tarea.descripcion = nueva_descripcion
        tarea.estado = nuevo_estado

        db.commit()
        print(f"{COLOR_VERDE}Tarea actualizada correctamente{COLOR_CIERRE}")
    except Exception as e:
        db.rollback()
        print(f"{COLOR_ROJO}Error al actualizar la tarea: {e}{COLOR_CIERRE}")
    finally:
        db.close()
        input(f"\n{COLOR_VERDE}Pulsa intro para continuar{COLOR_CIERRE}")

def eliminar_tarea():
    limpiar_pantalla()
    id_tarea = pedir_id()
    db = SessionLocal()
    try:
        tarea = db.query(Tarea).filter(Tarea.id_tarea == id_tarea).first()
        if not tarea:
            print(f"{COLOR_ROJO}Tarea no encontrada.{COLOR_CIERRE}")
            return

        mostrar_tarea(tarea, "Eliminar Tarea")
        confirmar = input(f"{COLOR_CYAN}¿Estás seguro que deseas eliminar esta tarea? (s/n): {COLOR_CIERRE}").lower()
        if confirmar in ["s", "sí", "si"]:
            db.delete(tarea)
            db.commit()
            print(f"{COLOR_VERDE}Tarea eliminada correctamente.{COLOR_CIERRE}")
        else:
            print(f"{COLOR_ROJO}Operación cancelada.{COLOR_CIERRE}")
    except Exception as e:
        db.rollback()
        print(f"{COLOR_ROJO}Error al eliminar la tarea: {e}{COLOR_CIERRE}")
    finally:
        db.close()
        input(f"\n{COLOR_VERDE}Pulsa intro para continuar...{COLOR_CIERRE}")

def pedir_id():
    while True:
        valor_id_str = input(f"{COLOR_CYAN}Introduce ID de la tarea: {COLOR_CIERRE}")
        if not valor_id_str.strip():
            print(f"{COLOR_ROJO}El ID no puede estar vacío.{COLOR_CIERRE}")
            continue
        try:
            valor_id = int(valor_id_str)
            if valor_id < 1:
                print(f"{COLOR_ROJO}El ID debe ser un número positivo.{COLOR_CIERRE}")
                continue
            return valor_id
        except ValueError:
            print(f"{COLOR_ROJO}ID no válido, debe ser un valor numérico.{COLOR_CIERRE}")

def mostrar_tarea(tarea, titulo="Información de la tarea"):
    print(f"\n------------------------- {COLOR_CYAN}{titulo}{COLOR_CIERRE} -----------------------------")
    print(f"{COLOR_CYAN}{'ID:':<15}{COLOR_CIERRE}{str(tarea.id_tarea)}")
    print(f"{COLOR_CYAN}{'Título:':<15}{COLOR_CIERRE}{tarea.titulo}")
    print(f"{COLOR_CYAN}{'Descripción:':<15}{COLOR_CIERRE}{tarea.descripcion:}")
    print(f"{COLOR_CYAN}{'Estado:':<15}{COLOR_CIERRE}{'EN CURSO' if tarea.estado == 1 else 'FINALIZADA'}")
    print("------------------------------------------------------------------------")
 

def buscar_tareas():
    limpiar_pantalla()
    consulta = input(f"{COLOR_CYAN}¿Qué tareas quieres buscar? {COLOR_CIERRE}")
    db = SessionLocal()
    try:
        tareas = db.query(Tarea).filter(
            or_(
                Tarea.titulo.ilike(f"%{consulta}%"),
                Tarea.descripcion.ilike(f"%{consulta}%")
            )
        ).all()

        if not tareas:
            print(f"{COLOR_ROJO}No se encontraron tareas que coincidan con tu búsqueda.{COLOR_CIERRE}")
        else:
            print(f"\n--- {COLOR_CYAN}Resultados de la búsqueda{COLOR_CIERRE} ---")
            print(f"{COLOR_CYAN}{'Id':<3} {'Título':<40} {'Descripción':<60} {'Estado':<10}{COLOR_CIERRE}")
            print("-" * 115)
            for tarea in tareas:
                estado = "EN CURSO" if tarea.estado == 1 else "FINALIZADA"
                print(f"{tarea.id_tarea:<3} {tarea.titulo:<40} {tarea.descripcion:<60} {estado:<10}")

        return tareas
    finally:
        db.close()
        input(f"\n{COLOR_VERDE}Pulsa intro para continuar...{COLOR_CIERRE}")
