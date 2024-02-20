from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import User

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        url = request.get_full_path()
        if (
            url.startswith('/admin')
            or url.startswith('/login') 
            or url.startswith('/signup')
        ):
            return self.get_response(request)
        # Check if the 'Authorization' header is present in the request
        authorization_header = request.headers.get('Authorization')
        
        if authorization_header and authorization_header.startswith('Bearer '):
            # Extract the token from the 'Authorization' header
            token = authorization_header.split(' ')[1]
            
            try:
                # Decode the token and get user data
                token_data = AccessToken(token).payload
                user = User.objects.get(id=token_data.get('user_id'))
                
            except Exception as e:
                # Handle token decoding errors
                response = Response({"message": "Invalid Token"}, status=400)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response
        else:
            response = Response({"message": "Invalid Token"}, status=400)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response

        # Continue processing the request
        response = self.get_response(request)
        return response