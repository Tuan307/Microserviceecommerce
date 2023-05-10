from rest_framework import serializers
from .models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'account', 'fullname', 'address',
                  'dob', 'email', 'phone', 'password','type']