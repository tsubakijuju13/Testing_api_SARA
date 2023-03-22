from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #Ahora realizo la busqueda en el modelo Usuario
        #query = list()

        #Devuelvo los clains en el token para ser convertidos . . .
        token['username'] = user.username
        token['email'] = user.email

        return token