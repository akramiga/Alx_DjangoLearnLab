from rest_framework import serializers
from.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password  # Import hashers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})  # Add password2

    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2','bio','profile_picture') # Include all relevant fields
        

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data['password1'] = make_password(validated_data.pop('password1'))  # Hash the password
        validated_data.pop('password2')
        user = CustomUser.objects.create(**validated_data)
        Token.objects.create(user=user)  # create a token for the user automatically
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)  # Or email, depending on your authentication
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)  # Only expose the token 'key' in the API.