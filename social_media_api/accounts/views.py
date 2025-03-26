from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import  CustomUserSerializer,RegistrationSerializer,LoginSerializer,TokenSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer


# Create your views here.
class RegistrationAPIView(generics.CreateAPIView):
    """
    Registers a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #token, _ = Token.objects.get_or_create(user=user) #token created in serializer
        return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)



class LoginAPIView(APIView):
    """
    Logs in an existing user and returns an authentication token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    """
    Logs out the user by deleting their token.
    Requires authentication (e.g., using TokenAuthentication).
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_authenticated:
            try:
                request.user.auth_token.delete()
                return Response({'message': 'Successfully logged out.'}, status=status.HTTP_204_NO_CONTENT)
            except AttributeError:
                return Response({'error': 'Token not found for this user.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response({'error': 'Not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileAPIView(APIView):
    """
    Retrieves data for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)