from .models import Article

from rest_framework import serializers


class ArticleSerializers(serializers.ModelSerializer):
    """Article数据序列化器"""

    class Meta:
        model = Article
        fields = '__all__'