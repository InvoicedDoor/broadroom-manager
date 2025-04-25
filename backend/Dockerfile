FROM python:3.11-slim AS development

# Actualizar paquetes y aplicar parches de seguridad
RUN apt update && apt upgrade -y && apt clean && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el código fuente al contenedor
COPY . .

# Crear un entorno virtual e instalar dependencias
RUN python -m venv venv && \
    sh venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de la aplicación
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]