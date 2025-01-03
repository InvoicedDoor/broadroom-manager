from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from users.models import User

class VerifyAuthentication(BasePermission):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None
        
        try:
            token = token.split(' ')[1] if ' ' in token else token
            token_obj = Token.objects.get(key=token)
            return (token_obj, None)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Token inválido.")
        
    def authenticate_header(self, request):
        return 'Bearer'