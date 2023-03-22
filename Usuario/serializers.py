from rest_framework import serializers
from .models import *

#Serializador para los usuarios:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'