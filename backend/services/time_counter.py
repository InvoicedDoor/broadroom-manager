from django.utils import timezone
from datetime import datetime

# Función para calcular la hora de finalización reglamentaria
def set_max_time():
    #try:
        # # time_now = time.localtime()
        # # year = time_now.tm_year
        # # month = len_two(time_now.tm_mon)
        # # day = len_two(time_now.tm_mday)
        # # hour = len_two(time_now.tm_hour + 2)
        # # minute = len_two(time_now.tm_min)
        # # second = len_two(time_now.tm_sec)
        time_now = datetime.localtime()
        year = time_now.tm_year
        month = time_now.tm_mon
        day = time_now.tm_mday
        hour = time_now.tm_hour + 2
        minute = time_now.tm_min
        second = time_now.tm_sec
        formated_time = f'{year}-{month}-{day}T{hour}:{minute}:{second}'
        return formated_time
    #except Exception as ex:
    #    return "No se pudo ejecutar"

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