from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'designation']
    
    def get_role(self, obj):
        role = obj.role_set.all()
        role_li = []
        for i in role:
            role_li.append(i.name)
        return role_li


class UserSerializerPost(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    designation = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'designation']
    
    def get_role(self, obj):
        role = obj.role_set.all()
        role_li = []
        for i in role:
            role_li.append(i.name)
        return role_li

    def get_designation(self, obj):
        designation = obj.designation.name
        return designation


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['name', 'description', 'designation_head']

class DesignationHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignationHead
        fields = ['name']


