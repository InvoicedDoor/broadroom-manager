from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from datetime import time, datetime
from django.utils import timezone
from django.db import connection
from services.time_counter import auto_delete_rows
from .serializer import ReservationSerializer
from .models import Reservation

# Create your views here.
class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [permissions.AllowAny]
    
    # Modificación de la función GET para obtener todos los valores
    def list(self, request, *args, **kwargs):
        return Response(self.get_reservations(request), status.HTTP_200_OK)
    
    # Módificación de la función para el método POST
    def create(self, request, *args, **kwargs):
        print(request.data)
        # Variables iniciales para trabajar la función
        start_time = request.data['start_time']
        finish_time = request.data['finish_time']
        print(f"{start_time}, {finish_time}, {datetime.now()}")
        serializer = self.get_serializer(data=request.data)
        duration = datetime.fromisoformat(finish_time) - datetime.fromisoformat(start_time)
        
        # Validar que la hora de inicio no sea antes de la hora de registro
        if not self.validate_start_hour(start_time):
            return Response({
                "status": "error",
                "message": "La hora de inicio no es válida."
            })
        
        # Validar que la hora de finalización no sea antes de la hora de iniciación y no sea mayor a 2 horas
        if not self.validate_finish_hour(start_time, finish_time, duration.seconds):    
            return Response({
                "status": "error",
                "message": "La hora de término no es válida."
            })
        
        if Reservation.objects.filter(broadrooms_id=request.data.get('broadrooms_id')).exists():
            return Response({
                'status': 'error',
                'message': 'La sala ya esta reservada.'
                }, status.HTTP_409_CONFLICT)
            
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        auto_delete_rows(duration.seconds, start_time, serializer.data['id'])
        return Response({
            "status": "success",
            "message": "Registro realizado con éxito."
            }, status.HTTP_201_CREATED)
        
    # Denegación del acceso al método PUT y PATCH
    def update(self, request, *args, **kwargs):
        return Response({
            "status":"error",
            "message":"Método no permitido."
            }, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # Modificación del método GET para obtener valores específicos siguiendo algunas reglas de validación
    def retrieve(self, request, *args, **kwargs):
        return Response({
            "status": "error",
            "message": "Método no permitido"
            }, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # Modificación del comportamiento del método DELETE
    def destroy(self, request, pk=None, *args, **kwargs):
        res = self.delete_reservation(pk)
        if res:
            return Response({
                "status": "success",
                "message": "Reservación eliminada con éxito.",

                }, status.HTTP_204_NO_CONTENT)
        return Response({
                "status": "error",
                "message": "La reservación no se encontró.",
                
                }, status.HTTP_404_NOT_FOUND)
    
    @classmethod
    # Cuntar el tiempo de desde el inicio al final
    def difference_time(self, start_time, finsih_time):
        if start_time < finsih_time:
            return finsih_time-start_time
        else:
            return (24-start_time)+finsih_time

    def validate_availability(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute('''SELECT * FROM reservations_reservation 
                                          WHERE start_time=%s''', [request.data['start_time']])
                row = cursor.fetchone()
            return row
        except Exception as ex:
            return "Error en la conexión"
        finally:
            cursor.close()
    
    # Comprobar si la hora ingresada es después al tiempo actual
    def validate_start_hour(self, date):
        if datetime.fromisoformat(date) > datetime.now():
            return True
        return False
    
    # Validar que la hora de finalización sea mayor al horario de inicio y que no sea mayor a 2 horas a partir del inicio
    def validate_finish_hour(self, start_time, finsih_time, duration):
        try:
            if duration < 7200:
                if datetime.fromisoformat(finsih_time) > datetime.fromisoformat(start_time):
                    if datetime.fromisoformat(start_time) > datetime.now():
                        return True
                    return False
                return False
            return False
        except Exception as ex:
            return False
    
    # Dar formato datetime a la entrada ingresada por el usuario
    def formated_datetime(self, string_time):
        string_date = datetime.now().date()
        return datetime.combine(string_date, time.fromisoformat(string_time)).isoformat()
    
    # Obtener las reservaciones
    def get_reservations(self, request):
        reservations = []
        try:
            with connection.cursor() as cursor:
                cursor.execute('''SELECT r.id, u.name, b.name, r.start_time, r.finish_time FROM reservations_reservation r INNER JOIN users_user u ON u.user_id=r.users_id_id INNER JOIN broadrooms_broadroom b ON b.broadroom_id=r.broadrooms_id_id''')
                #cursor.execute("select * from reservations_reservation")
                raw = cursor.fetchall()
                for row in raw:
                    reservations.append({
                    "id": row[0],
                    "user": row[1],
                    "room": row[2],
                    "start_time": row[3],
                    "finish_time": row[4]
                    })
            return {
                "status": "success",
                "message": reservations
                }
        except Exception as ex:
            return {
                "status": "error",
                "message": "Error en la conexión"
                }
        finally:
            cursor.close()
    
    # Función para eliminar las reservaciones de manera manual
    def delete_reservation(self, id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reservations_reservation WHERE id=%s", [id])
                raw = cursor.fetchone()
                if raw:
                    cursor.execute("DELETE FROM reservations_reservation WHERE id=%s", [id])
                    return True
                return False
        except Exception as ex:
            pass
        finally:
            cursor.close()