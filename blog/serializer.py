from .models import Article

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    """User数据序列化器"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff',
                  'is_superuser')


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
