#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from user.models import UserProfile

# Create your models here.


class Problem(models.Model):

    title = models.CharField(max_length=80)

    publicizer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    description = models.TextField(default='')
    input_format = models.TextField(default='')
    output_format = models.TextField(default='')
    example = models.TextField(default='')
    limit_and_hint = models.TextField(default='')

    time_limit = models.IntegerField(default='')
    memory_limit = models.IntegerField(default='')

    additional_file_id = models.IntegerField(blank=True, null=True)

    # 文件输出输入部分
    file_io = models.BooleanField(default=False)
    file_io_input_name = models.TextField(blank=True, null=True)
    file_io_output_name = models.TextField(blank=True, null=True)

    # 统计数字
    ac_num = models.IntegerField(default=0)
    submit_num = models.IntegerField(default=0)

    # 是否公开
    is_public = models.BooleanField(default=True)