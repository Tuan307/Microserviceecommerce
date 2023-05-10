from rest_framework import serializers
from .models import CartModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ['productId','userId']