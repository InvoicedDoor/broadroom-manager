from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from io import BytesIO
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import status
from users.models import User
from .serializer import LoginSerializer, RegisterSerializer

# Create your views here.
class AuthUsersView(ViewSet):
    queryset = User.objects.all()
    write_only_fields = ['password']

    @action(detail=False, methods=["POST"])
    def login(aelf, request):
        data = JSONParser().parse(BytesIO(request.body))
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.validated_data['user']

        if not user.check_password(data['password']):
            return Response({'message': 'Credenciales incorrectas'}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)

        if token:
            return Response({
                "message": "Login exitoso",
                'token': f"Bearer {token.key}",
                'user_id': user.user_id,
                'name': user.name
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["POST"])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():

            if User.objects.filter(email=request.data['email']).exists():
                raise ValidationError({"message": "El correo ya existe."})

            user = serializer.save()

            token = Token.objects.create(user=user)

            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({
            "status": "error",
            "message": "Método inactivo."
        }, status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request):
        return Response({
            "status": "error",
            "message": "Método inactivo."
        }, status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request):
        return Response({
            "status": "error",
            "message": "Método inactivo."
        }, status.HTTP_405_METHOD_NOT_ALLOWED)
