from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Register
# Create your views here.

@api_view(['POST'])
def post(request):
    serializer = RegisterSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "Successfully registered"}, status=status.HTTP_201_CREATED)
    return Response({"message" : "Registration failed"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        find_user = Register.objects.get(email=email) #now this holds the entier current document
        if find_user.password == password:
            return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Login Failure, Incorrect Password"}, status=status.HTTP_401_UNAUTHORIZED)
    except Register.DoesNotExist:
        return Response({"message": "Login Failure, User not found"}, status=status.HTTP_404_NOT_FOUND)