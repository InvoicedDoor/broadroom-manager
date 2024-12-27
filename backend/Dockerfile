FROM python:3.11

RUN apt update \
    && apt-get install -y --no-install-recommends \
    postgresql-client\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
RUN python manage.py makemigrations
CMD ["python", "manage.py", "runserver", "0.0.0.0:4000"]