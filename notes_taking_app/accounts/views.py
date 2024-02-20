from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken


@permission_classes([AllowAny])
@csrf_exempt
@api_view(['POST'])
def signup_view(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Create a new user
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
@csrf_exempt
@api_view(['POST'])
def login_view(request):
    
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        token_data = {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
            'user_data': user_serializer.data
        }

        return Response(token_data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(["POST"])
@permission_classes([AllowAny])
def test_view(request):
    import ipdb; ipdb.set_trace()
    pass