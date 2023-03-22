from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *

#View del Usuario
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
