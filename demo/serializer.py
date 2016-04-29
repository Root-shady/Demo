from rest_framework import serializers
from django.db import models

#from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('username', 'email', 'password', 'sex')
				
