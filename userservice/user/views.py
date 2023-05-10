from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer


class UserModelListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    #post get all


class UserModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    # get one-put-patch