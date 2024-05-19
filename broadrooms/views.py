from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from http import HTTPMethod
from .serializer import BroadroomsSerializer
from .models import Broadroom

# Create your views here.
class BroadroomView(viewsets.ModelViewSet):
    
    @action(detail=True, methods=[HTTPMethod.POST])
    def reserve_broadrooms(self, request):
        broadroom = self.get_object()
        serializer = BroadroomsSerializer(data=request.data)
        exist = self.queryset.get(request.data)
        if not exist:
            if serializer.is_valid():
                broadroom.reserve_broadroom(serializer.validated_data)
                broadroom.save()
                return Response({'message': 'User created'})
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Ya esta reservado'}, 
                            status.HTTP_409_CONFLICT)