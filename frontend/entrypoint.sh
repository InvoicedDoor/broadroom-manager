#!/bin/bash

# Iniciar PM2 para ejecutar la aplicación Node.js
pm2 start npm --name broadroom_manager-frontend -- run dev

# Iniciar NGINX en modo foreground
nginx -g 'daemon off;'
