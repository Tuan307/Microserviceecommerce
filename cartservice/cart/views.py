from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import CartModel
from .serializers import UserModelSerializer
from django.shortcuts import get_list_or_404
from rest_framework.response import Response

class UserModelListCreateView(generics.ListCreateAPIView):
    queryset = CartModel.objects.all()
    serializer_class = UserModelSerializer
    #post get all


@api_view(['GET'])
def get(request, userId):
    if request.method == 'GET':
        carts = get_list_or_404(CartModel, userId=userId)
        data = {}
        productIds = []
        for cart in carts:
            productIds.append(cart.productId)
        data['productId'] = productIds
        return Response(data=data, status=200)


class UserModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartModel.objects.all()
    serializer_class = UserModelSerializer
    # get one-put-patch