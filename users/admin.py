from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'level')
    actions = ['approve', 'withdraw']

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def approve(self, request, queryset):
        queryset.update(level=2)

    approve.short_description = "开放权限"

    def withdraw(self, request, queryset):
        queryset.update(level='1')
    withdraw.short_description = '撤回权限'


admin.site.register(Profile, ProfileAdmin)
