#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
有关User的序列器
"""
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    """
    User数据序列化器
    适用于各种ForeignKey查找
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff',
                  'is_superuser')


class UserLoginSerializer(serializers.ModelSerializer):
    """用于用户登陆"""

    class Meta:
        pass


class UserRegisterSerializer(serializers.ModelSerializer):
    """用于用户注册"""

    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(
        required=True, allow_blank=False, write_only=True, min_length=8)

    def create(self, validated_data):
        """重载create"""
        user = super(UserRegisterSerializer,
                     self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')
