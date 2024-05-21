from rest_framework import viewsets, permissions, status,request
from rest_framework.response import Response
from datetime import time, datetime
from django.db import connection
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
        serializer = self.get_serializer(data=request.data)
        if self.validate_start_hour(request.data['start_time']):
            return Response({
                "status": "error",
                "message": "La hora de inicio no es válida."
            })
        if self.validate_finish_hour(start_date=request.data['start_time'], finish_date=request.data['finish_time']):
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
        return Response({
            "status": "success",
            "message": "serializer.data"
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
            
    def validate_start_hour(self, date):
        if time.fromisoformat(date) < datetime.now().time():
            return True
        return False
    
    def validate_finish_hour(self, start_date, finish_date):
        try:
            if int(time.fromisoformat(start_date).hour+2) > 23:
                hour_finish = int(time.fromisoformat(start_date).hour+2)-24
            else:
                hour_finish = time.fromisoformat(start_date).hour+2
            minute=time.fromisoformat(start_date).minute
            second=time.fromisoformat(start_date).second
            max_time = time(hour=hour_finish, minute=minute, second=second).isoformat()
            if time.fromisoformat(finish_date) > time.fromisoformat(max_time):
                return True
            return False
        except Exception as ex:
            return False
        
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
            
    def delete_reservation(self, id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM reservations_reservation WHERE id=%s", [id])
                raw = cursor.fetchone()
                print(raw)
                if raw:
                    cursor.execute("DELETE FROM reservations_reservation WHERE id=%s", [id])
                    return True
                return False
        except Exception as ex:
            pass
        finally:
            cursor.close()