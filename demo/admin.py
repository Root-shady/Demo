from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, FileManager

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('sex', 'image', 'is_admin')

class FileManagerAdmin(admin.ModelAdmin):
	list_display = ('id', 'path')

UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined')
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FileManager, FileManagerAdmin)
