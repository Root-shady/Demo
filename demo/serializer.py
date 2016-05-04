from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

#from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password','email')
	
class UserProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = UserProfile
		fields = ('id', 'user', 'sex','image')

	
	def create(self, validated_data):
		"""
		Create and return a new "UserProfile" instance, given the validated data
		"""
		user = User.objects.create_user(
			email = validated_data['user']['email'],
			username = validated_data['user']['username'],
			password = validated_data['user']['password'],
		)
		#user,created = User.objects.get_or_create(username, email, password)
		# Need a better way to do this
		return UserProfile.objects.create(user=user, sex=validated_data['sex'], 
			image=validated_data['image'])
		
	def update(self, instance, validated_data):
		"""
		Update and return an existing 'UserProfile' instance, given the validated
		data
		"""
		instance.user.username = validated_data['user'].get('username', instance.user.username)
		if 'password' in validated_data['user']:
			instance.user.set_password(validated_data['user']['password'])
		instance.user.email = validated_data['user'].get('email', instance.user.email)

		# Save in the User model
		instance.user.save()

		instance.sex = validated_data.get('sex', instance.sex)
		instance.image = validated_data.get('image', instance.image)
		instance.save()
		return instance

