from rest_framework import serializers

class CartSerializer(serializers.Serializer):
    productId = serializers.IntegerField()
    userId = serializers.IntegerField()