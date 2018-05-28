from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import viewsets, permissions

# local
from .serializer import ArticleSerializers
from .models import Article
from user.permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
