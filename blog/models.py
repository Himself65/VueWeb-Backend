from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """博客"""

    # 作者
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='作者')

    title = models.CharField(max_length=50, verbose_name='标题')

    head_img_url = models.URLField(
        blank=True, null=True, verbose_name='封面图片地址')

    content = models.TextField(verbose_name='内容')

    created_time = models.DateField(auto_now_add=True, verbose_name='创建时间')

    update_time = models.DateField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


# TODO
# 随后添加本地存储图片
# class Image(models.Model):
#     """图片"""

#     image = models.ImageField(
#         upload_to='pic_folder/', default='pic_folder/None/404.jpg')

#     # author = models.ForeignKey(User, on_delete=models.CASCADE)

#     # title = models.CharField(max_length=100)

#     # caption = models.CharField(max_length=250, blank=True, null=True)

#     # source = models.ImageField(upload_to='photos')

#     def __str__(self):
#         return self.title

#     def __unicode__(self):
#         return self.title

#     def get_absolute_url(self):
#         return ('photo_detail', None, {'object_id': self.id})
