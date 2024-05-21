from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import BroadroomsSerializer
from .models import Broadroom

# Create your views here.
class BroadroomView(viewsets.ModelViewSet):
    queryset = Broadroom.objects.all()
    serializer_class = BroadroomsSerializer
            
