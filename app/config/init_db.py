import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.config.database import Base, engine
from app.models.fruits import Fruit

# Crear todas las tablas en la base de datos
print("Creando tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas exitosamente.")