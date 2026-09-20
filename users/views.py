from django.shortcuts import render
from rest_framework import generics
from users.models import CustomUser
from users.serializers import CustomUserSerializer


# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer