from rest_framework import serializers
from .models import product_details


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_details
        fields = ['product_id','product_category',
'product_name',
'availability',
'price',
'productType',
'size',]