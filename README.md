# PruebaFastAPI
Este proyecto es un ejemplo práctico utilizando FastAPI, una librería moderna y rápida para construir APIs en Python. Incluye funcionalidades de manejo de datos, validaciones, y generación automática de documentación.

Estructura del Proyecto

TallerFastAPI-main/
├── app/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── fruits.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── fruits.py
│   │   └── openai.py
│   ├── endpoints.py
│   └── openia.py
├── requeriments.txt
├── README.md
└── database.sqlite

app/config/: Configuración general del proyecto (base de datos, variables de configuración).

app/models/: Definición de modelos de datos.

app/schemas/: Esquemas de datos utilizados para validaciones y serialización.

app/endpoints.py: Definición de los endpoints principales de la API.

database.sqlite: Base de datos SQLite utilizada en el proyecto.

requeriments.txt: Lista de dependencias del proyecto.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.9 o superior.

Pip (gestor de paquetes de Python).

Virtualenv (opcional pero recomendado).

## Instalación

Clona el repositorio:

git clone https://github.com/tu_usuario/tallerfastapi.git
cd tallerfastapi

## Crea y activa un entorno virtual (opcional):

python -m venv venv
# En Windows
.\venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate

## Instala las dependencias:

pip install -r requeriments.txt

## Inicia el servidor:

python -m uvicorn app.endpoints:app --reload

## Accede a la API:

Documentación interactiva (Swagger UI): http://127.0.0.1:8000/docs

Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc

## Funcionalidades

CRUD de frutas: Manejo básico de datos de frutas (crear, leer, actualizar, eliminar).

Integración con OpenAI: Procesamiento de preguntas usando un esquema de ejemplo.

Base de datos SQLite: Persistencia de datos con SQLAlchemy.

## Configuración

El archivo app/config/config.py contiene la configuración básica del proyecto. Si necesitas ajustar algo, asegúrate de modificar ese archivo según tus necesidades.

# Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún problema o deseas mejorar algo, no dudes en abrir un issue o enviar un pull request.

¡Gracias por explorar este proyecto! Si tienes alguna pregunta, no dudes en contactarme o abrir un issue en el repositorio.
