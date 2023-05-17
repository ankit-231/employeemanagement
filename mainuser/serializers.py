from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email',]


class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

