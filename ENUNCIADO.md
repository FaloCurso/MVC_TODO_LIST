
# 🧩 Proyecto: To-Do List por consola con arquitectura MVC

---

## 🎯 Objetivo

Desarrollar una aplicación por consola que permita gestionar tareas (crear, listar, actualizar, eliminar) utilizando **Python**, **PostgreSQL**, **SQLAlchemy** y **arquitectura MVC**, sin usar frameworks.

Este ejercicio servirá como base para entender cómo se estructura un backend y facilitar la posterior transición a frameworks como Django.

---

## 🧠 Aprendizajes clave

- En este ejercicio tendrás que poner en práctica lo aprendido y hacer un proceso de investigación por parejas. Pero tendras pistas en los enunciados así como en el README.md
- Uso de entornos virtuales y organización profesional de un proyecto
- Conexión a una base de datos PostgreSQL desde Python
- ORM con SQLAlchemy para definir modelos y operar con la base de datos
- Uso de Alembic para gestionar migraciones
- Implementación del patrón arquitectónico MVC
- Uso de consola como interfaz de usuario (`input()` / `print()`)

---

## 📋 Requisitos funcionales

1. El usuario debe poder:
   - ✅ Crear una tarea con título y descripción
   - ✅ Ver todas las tareas existentes
   - ✅ Consultar una tarea por ID
   - ✅ Actualizar una tarea existente (título, descripción o estado)
   - ✅ Eliminar una tarea

2. Las tareas deben persistirse en una base de datos PostgreSQL (`todo_db`).

---

## 🔧 Restricciones técnicas

- ❌ No se debe usar ningún framework web (como Flask o Django)
- ✅ La lógica debe estar separada en:
  - `models/`: clases que representan la base de datos
  - `controllers/`: lógica del negocio
  - `views/`: menú por consola
  - `database/`: configuración y conexión
- ✅ Usar `pg8000` como driver de PostgreSQL
- ✅ Usar Alembic para crear y aplicar migraciones -> Más limpio.

---

## 🗂️ Entrega esperada

Estructura del proyecto:

```
todo_list/
├── models/              # Modelos SQLAlchemy
├── controllers/         # Funciones CRUD
├── database/            # Conexión a la base de datos
├── views/               # Menú de interacción por consola
├── alembic/             # Migraciones de base de datos
├── requirements.txt     # Dependencias
├── README.md            # Documentación técnica
├── ENUNCIADO.md         # (Este archivo)
```

---

## 🧪 Criterios de evaluación

- ✅ Separación clara y coherente en capas (MVC)
- ✅ Funcionamiento completo del CRUD
- ✅ Uso adecuado de SQLAlchemy y Alembic
- ✅ Código limpio, legible y probado
- ✅ Interacción clara a través del menú en consola

---

## ✨ Bonus (opcional)

- Validación de entradas del usuario
- Decorar el menú con estilo
- Colores o mensajes amigables
- El Bonus del Bonus que Nico quiera implementar... 😉

---

¡Mucho ánimo y a disfrutar de aprender a aprender código! 🐍💡
