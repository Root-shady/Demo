from django.contrib import admin
from .models import UserProfile, FileManager
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'password','email', 'sex', 'image', 'is_admin')

class FileManagerAdmin(admin.ModelAdmin):
	list_display = ('id', 'path')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FileManager, FileManagerAdmin)
