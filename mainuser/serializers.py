from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    designation = serializers.SerializerMethodField()
    designation_head = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'designation', 'designation_head']
    
    def get_role(self, obj):
        role = obj.role_set.all()
        role_li = []
        for i in role:
            role_li.append(i.name)
        return role_li
    
    def get_designation(self, obj):
        try:
            designation = obj.designation.name
        except AttributeError:
            designation = None
        return designation
    
    def get_designation_head(self, obj):
        try:
            designation_head = obj.designation.designation_head.name
        except AttributeError:
            designation_head = None
        return designation_head


class UserSerializerPost(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    designation = serializers.SerializerMethodField()
    # designation_head = serializers.SerializerMethodField()

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
        try:
            designation = obj.designation.name
        except AttributeError:
            designation = None
        return designation


class RoleSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    class Meta:
        model = Role
        fields = ['name', 'users']
    
    def get_users(self, obj):
        users_qs = obj.user_role.all()
        users = list()
        for i in users_qs:
            users.append(i.username)
        return users

class DesignationSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    designation_head = serializers.SerializerMethodField()
    class Meta:
        model = Designation
        fields = ['name', 'description', 'designation_head', 'users']
    
    def get_users(self, obj):
        users_qs = obj.customuser_set.all()
        users = list()
        for i in users_qs:
            users.append(i.username)
        return users

    def get_designation_head(self, obj):
        try:
            designation_head = obj.designation_head.name
        except AttributeError:
            designation_head = None
        return designation_head

class DesignationHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignationHead
        fields = ['name']


