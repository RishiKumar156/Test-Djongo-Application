from .models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Register
        fields = ('username', 'email', 'password')
        
    def create(self,validate_data):
        user = Register.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            password = validate_data['password']
        )
        return user