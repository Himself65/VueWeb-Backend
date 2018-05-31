from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
# local
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = '用户资料'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
