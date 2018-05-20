from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import viewsets

# local
from .serializer import ArticleSerializers
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
