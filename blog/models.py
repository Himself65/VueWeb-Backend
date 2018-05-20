from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """博客"""

    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)

    content = models.TextField()

    created_time = models.DateField(auto_now_add=True)

    update_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
