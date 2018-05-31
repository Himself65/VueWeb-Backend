#!/usr/bin/python
# -*- coding: utf-8 -*-

from .models import Problem

from rest_framework import serializers
from django.contrib.auth.models import User
from user.serialiszer import UserSerializers


class ProblemSerializers(serializers.ModelSerializer):
    """Problem序列化器"""
    pass