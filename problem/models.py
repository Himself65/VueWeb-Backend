#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from user.models import User

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=80, verbose_name='标题')
    publicizer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='题目提供者')
    description = models.TextField(default='', verbose_name='描述')
    input_format = models.TextField(default='', verbose_name='输入格式')
    output_format = models.TextField(default='', verbose_name='输出格式')
    example = models.TextField(default='', verbose_name='样例')
    limit_and_hint = models.TextField(default='', verbose_name='提示')
    time_limit = models.IntegerField(default=int(0), verbose_name='时间限制')
    memory_limit = models.IntegerField(default=int(0), verbose_name='内存限制')
    additional_file_id = models.IntegerField(
        blank=True, null=True, verbose_name='附加文件')
    file_io = models.BooleanField(default=False, verbose_name='是否特定输入输出格式')
    file_io_input_name = models.TextField(
        blank=True, null=True, verbose_name='输入文件名')
    file_io_output_name = models.TextField(
        blank=True, null=True, verbose_name='输出文件名')
    ac_num = models.IntegerField(default=int(0), verbose_name='通过人数')
    submit_num = models.IntegerField(default=int(0), verbose_name='总提交数')
    is_public = models.BooleanField(default=True, verbose_name='是否公开题目')
