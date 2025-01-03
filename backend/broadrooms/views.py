from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import BroadroomsSerializer
from .models import Broadroom
from services.middleware.authenticate_verify import VerifyAuthentication

# Create your views here.
class BroadroomView(viewsets.ModelViewSet):
    queryset = Broadroom.objects.all()
    serializer_class = BroadroomsSerializer
    authentication_classes = [VerifyAuthentication]
    
    def retrieve(self, request, *args, **kwargs):
        return Response({
            "status": "error",
            "message": "Método inactivo."
        }, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response({
            "status": "error",
            "message": "Método inactivo."
        }, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({
            "status": "error",
            "message": "Método inactivo."
        }, status.HTTP_405_METHOD_NOT_ALLOWED)
            
