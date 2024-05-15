# Usa la imagen base de Python 3.8 en Alpine Linux
FROM python:3.8-alpine

# Establece el directorio de trabajo dentro del contenedor
#WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . .

RUN apk update
RUN apk add --no-cache nginx
RUN rm /etc/nginx/http.d/default.conf
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak

COPY nginx.conf /etc/nginx/nginx.conf

# Instala las dependencias de Flask
 
RUN apk add --no-cache curl
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación Flask
EXPOSE 80
EXPOSE 8080

# Ejecuta la aplicación Flask
#CMD ["python3", "app.py"]
#CMD ["nginx", "-g", "daemon off;"]
#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "wsgi:app"]
CMD ["sh", "-c", "gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app & nginx -g 'daemon off;'"]

