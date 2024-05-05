# Usa una imagen base de Python para Flask
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos y luego instala las dependencias
COPY /requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de la aplicación
COPY /app.py app.py

# Expone el puerto 3000 en el contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
