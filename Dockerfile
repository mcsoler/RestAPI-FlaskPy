# Usa la imagen base de Python 3.8 en Alpine Linux
FROM python:3.8-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . .

# Instala las dependencias de Flask
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# Ejecuta la aplicación Flask
CMD ["python3", "/home/gibgo/webservice/app/app.py"]
