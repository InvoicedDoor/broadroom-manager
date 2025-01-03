from rest_framework import serializers
from users.models import User
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class EnrollmentCounter(models.Model):
    count = models.IntegerField(default=0)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    enrollment = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'enrollment', 'username']
        read_only = ['user_id', 'date_joined', 'last_login']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)

        if not user.enrollment or not user.username:
            counter, created = EnrollmentCounter.objects.get_or_create(id=1)
            counter.count += 1
            counter.save()

            user.enrollment = f'RG-{str(timezone.now().year)[-2:]}{counter.count:04d}'
            user.username = f'user{counter.count:04d}'
        
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['user_id','name', 'email', 'is_active']
        read_only = 'user_id'

    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Debe proporcionar un correo y una contraseña.")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Credenciales incorrectas. Por favor, inténtalo de nuevo.")

        if not user.check_password(password):
            print("Contraseña incorrecta")
            raise serializers.ValidationError("Credenciales incorrectas. Por favor, inténtalo de nuevo.")
        
        if not user.is_active:
            raise serializers.ValidationError("Esta cuenta está inactiva.")
        
        attrs['user'] = user
        return attrs