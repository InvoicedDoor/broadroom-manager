from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        return Response({"You shouldn't do it"}, status.HTTP_405_METHOD_NOT_ALLOWED)
