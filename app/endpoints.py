from fastapi import FastAPI

app = FastAPI()

# Ruta de bienvenida personalizada
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la versión demo de la aplicación"}

# Ruta adicional para información sobre la demo
@app.get("/demo-info")
def demo_info():
    return {
        "title": "Taller FastAPI - Demo",
        "description": "Esta es una versión para demostrar las funcionalidades del proyecto.",
        "branch": "demo",
    }
