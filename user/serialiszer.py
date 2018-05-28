#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
有关User的序列器
"""
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    token = models.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
