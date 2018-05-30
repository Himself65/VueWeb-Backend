from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ViewSetMixin
from rest_framework.status import *
from rest_framework import mixins, viewsets

#local
from .serialiszer import UserLoginSerializer, UserRegisterSerializer


class UserRegisterViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    用户注册API
    '''
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        # 将post过来的数据传给UserRegisterSerializer进行序列化和验证
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        re_dict["username"] = user.username if user.username else user.username
        re_dict["success"] = '注册成功'
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class UserLoginViewSet():
    '''
    用户登陆API
    '''