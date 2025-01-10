# Imagen base
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias del proyecto
COPY requeriments.txt /app/requeriments.txt
COPY . /app


# Instalar dependencias
RUN pip install --no-cache-dir -r requeriments.txt

CMD ["uvicorn", "app.endpoints:app", "--host", "0.0.0.0", "--port", "8000"]



