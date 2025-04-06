FROM python:3.12-slim AS development

RUN apt update

WORKDIR /app

COPY . .

RUN sh venv/Scripts/activate && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:4000"]