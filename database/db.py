import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Asegúrate de que conecta a la base de datos correcta
DATABASE_URL = "postgresql+pg8000://postgres:1234@localhost/tareas_bd"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

