#!/usr/bin/python
# -*- coding: utf-8 -*-
from .models import Article

from rest_framework import serializers
from django.contrib.auth.models import User
from user.serialiszer import UserSerializers


class ArticleSerializers(serializers.ModelSerializer):
    """Article数据序列化器"""
    author = UserSerializers(many=False, read_only=True)

    class Meta:
        model = Article
        fields = (
            'author',
            'title',
            'head_img_url',
            'content',
            'created_time',
            'update_time',
        )
