from time import sleep
from threading import Thread
from django.db import connection
from datetime import datetime, timezone

# Función para calcular la hora de finalización reglamentaria
def set_max_time():
    try:
        time_now = datetime.now()
        year = time_now.tm_year
        month = time_now.tm_mon
        day = time_now.tm_mday
        hour = time_now.tm_hour + 2
        minute = time_now.tm_min
        second = time_now.tm_sec
        formated_time = f'{year}-{month}-{day}T{hour}:{minute}:{second}'
        return formated_time
    except Exception as ex:
        return "No se pudo ejecutar"

# Función para validar que los horarios sean correctos.
def validate_date(start_time, finish_time):
    is_valid = False
    formated_start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S')
    formated_finish_time = datetime.strptime(finish_time, '%Y-%m-%dT%H:%M:%S')
    min_hour = datetime.now()
    max_hour = formated_start_time.hour + 2
    if formated_start_time >= min_hour:
        if formated_finish_time.hour <= max_hour:
            is_valid = True
    
    return is_valid

# Función para dar formato de dos dígitos a meses, días, horas, minutos y segundos
def len_two(time):
    if len(str(time)) == 1:
            time = f'0{time}'
    return time

def count_seconds(seconds, start_time, id):
    try:
        while start_time:
            if start_time < datetime.now():
                break
            sleep(1)
        with connection.cursor() as cursor:
            for second in range(seconds+1):
                if second == seconds:
                    cursor.execute("DELETE FROM reservations_reservation WHERE id=%s", [id])
                    print(f"Registro eliminado a las {datetime.now()}")
                sleep(1)
    except Exception as ex:
        print(f"Hubo un error {ex}")
    finally:
        if cursor is not None:
            cursor.close()

# Función para automatizar el borrado de registros
def auto_delete_rows(seconds, start_time, id):
    thread = Thread(target=count_seconds, args=(seconds,start_time, id))
    thread.start()