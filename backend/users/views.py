from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
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