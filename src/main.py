import os
import sys
# Añadimos la ruta del directorio padre (crud_python) al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora importamos desde src.views
from views.task_view import mostrar_menu

if __name__ == "__main__":
    print("Iniciando aplicación de tareas...")
    mostrar_menu()