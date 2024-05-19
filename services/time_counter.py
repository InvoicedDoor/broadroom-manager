import time

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
        time_now = time.localtime()
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

def len_two(time):
    if len(str(time)) == 1:
            time = f'0{time}'
    return time