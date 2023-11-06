from rest_framework import serializers

class RegisterModel(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length = 150)
    password = serializers.CharField(max_length = 150)

class LoginModel(serializers.Serializer):
    email = serializers.EmailField(max_length = 150)
    password = serializers.CharField(max_length = 150)