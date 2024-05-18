from rest_framework import viewsets
from .serializer import ReservationSerializer
from .models import Reservation

# Create your views here.
class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()