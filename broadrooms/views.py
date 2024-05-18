from rest_framework import viewsets
from .serializer import BroadroomsSerializer
from .models import Broadroom

# Create your views here.
class BroadroomView(viewsets.ModelViewSet):
    serializer_class = BroadroomsSerializer
    queryset = Broadroom.objects.all()