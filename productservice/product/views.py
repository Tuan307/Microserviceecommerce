from django.shortcuts import render
from rest_framework import generics
from .models import product_details
from .serializers import UserModelSerializer
# Create your views here.
class UserModelListCreateView(generics.ListCreateAPIView):
    queryset = product_details.objects.all()
    serializer_class = UserModelSerializer
    #post get all


class UserModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_details.objects.all()
    serializer_class = UserModelSerializer
    # get one-put-patch