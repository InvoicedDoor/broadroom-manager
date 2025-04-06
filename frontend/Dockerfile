# FROM node:22

# # Configurar el directorio de trabajo
# WORKDIR /app

# # Instalar dependencias
# RUN apt update && apt install -y vim ssh

# COPY package*.json .

# RUN npm i

# # Copiar el código fuente al contenedor
# COPY . .

# # Instalar dependencias de Node.js

# # Instalar PM2 globalmente
# RUN npm i -g pm2

# RUN service ssh start

# RUN update-rc.d ssh defaults

# #RUN rm /etc/nginx/sites-available/*
# #RUN rm conf.d/default.conf

# FROM nginx AS development
# # Copiar el archivo de configuración de NGINX
# COPY --from=build /app/dist /usr/share/nginx/html

# # COPY nginx-api.conf /etc/nginx/sites-available/api

# # RUN ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled/

# # # Exponer el puerto 80
# # EXPOSE 80

# # # Usar un script para manejar múltiples procesos
# # # COPY entrypoint.sh /entrypoint.sh
# # # RUN chmod +x /entrypoint.sh
# # RUN pm2 start npm --name broadroom_manager-frontend -- run dev
# # # Configurar el script como punto de entrada
# # # ENTRYPOINT ["/entrypoint.sh"]
# CMD [ "nginx", "-g", "daemon off;" ]


FROM node:22-alpine3.18 AS build
WORKDIR /app
COPY ./package*.json /app/
RUN npm install
COPY . .
RUN npm run build

FROM nginx AS development
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]