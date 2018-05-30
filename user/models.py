#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """扩展User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    github = models.TextField()

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = "user_profile"