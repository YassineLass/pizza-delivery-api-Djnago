from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework import generics,status
from . import serializers



# Create your views here.

class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer
    def post(self,request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)    
