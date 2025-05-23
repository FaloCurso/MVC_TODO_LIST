import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import Column, Integer, String, Boolean
from database.db import Base

class Tarea(Base):
    __tablename__ = "tareas" 

    id_tarea = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=True)
    estado = Column(Boolean, nullable=False, default=True)
