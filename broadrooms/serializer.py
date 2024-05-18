from rest_framework import serializers
from .models import Broadroom

class BroadroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadroom
        fields = '__all__'
        read_only = 'broadroom_id'