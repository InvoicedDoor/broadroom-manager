from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'enrollment', 'email']
        read_only = ['date_joined', 'last_login', 'user_id']
        write_only = ['password']

    def create(self, validated_data):
        
        try:
            password = validated_data.pop('password')

            validated_data['password'] = make_password(password)
            
            return User.objects.create_user(**validated_data)
        except User.DoesNotExist:
            return User()
