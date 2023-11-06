from verification.models import Register , Login
from verification.serializer import RegisterModel
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Register(APIView):
    def post(self, request):
        input_data = RegisterModel(data= request.data)
        email = input_data.data['email']
        password = input_data.data['password']
        username = input_data.data['username']
        if input_data.is_valid():
            hash_password = make_password(password)
            register_user_in_db = Register(
                username = username, 
                email = email , 
                password = hash_password
            )
            register_user_in_db.save()
            return Response({"message" : "Success you're profile has been registered"} , status=status.HTTP_201_CREATED)
        else:
            return Response({"message" : "Inavlid data passed to register"}, status=status.HTTP_400_BAD_REQUEST)