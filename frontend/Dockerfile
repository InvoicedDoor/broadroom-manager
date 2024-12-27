FROM node:22

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar dependencias
RUN apt update && apt install -y vim nginx ssh

COPY package*.json .

RUN npm i

# Copiar el código fuente al contenedor
COPY . .

# Instalar dependencias de Node.js

# Instalar PM2 globalmente
RUN npm i -g pm2

RUN service ssh start

RUN update-rc.d ssh defaults

#RUN rm /etc/nginx/sites-available/*
#RUN rm conf.d/default.conf

# Copiar el archivo de configuración de NGINX
COPY nginx.conf /etc/nginx/sites-available/default

COPY nginx-api.conf /etc/nginx/sites-available/api

RUN ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled/

# Exponer el puerto 80
EXPOSE 80

# Usar un script para manejar múltiples procesos
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Configurar el script como punto de entrada
ENTRYPOINT ["/entrypoint.sh"]
