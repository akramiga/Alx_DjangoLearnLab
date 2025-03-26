from django.conf import settings
from rest_framework import serializers, viewsets, status, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView

# Get the user model
User = get_user_model()


# Serializers
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User  # Use get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2', 'bio', 'profile_picture')
        

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)  # Use get_user_model()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


# Views (APIView and Generics)
class RegistrationAPIView(generics.CreateAPIView):
    """
    Registers a new user.
    """
    queryset = User.objects.all() # Use get_user_model()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
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


class UserDataAPIView(APIView):
    """
    Retrieves data for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)