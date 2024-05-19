from rest_framework import viewsets, permissions
from users.models import User
from .serializer import ReservationSerializer
from .models import Reservation

# Create your views here.
class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [permissions.AllowAny]