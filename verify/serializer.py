from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.Serializer):
    class meta :
        model = Register
        fields = ('__all__')
        