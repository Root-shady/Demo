from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import UserProfile
from .serializer import UserProfileSerializer

@api_view(['GET', 'POST'])
def register(request, format=None):
	"""
	Create a new user
	"""
	if request.method == 'GET':
		users = UserProfile.objects.all()
		serializer = UserProfileSerializer(users, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = UserProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request, format=None):
	"""
	Login a user
	"""
	if request.method == 'POST':
		data = request.data
		password = data['password']
		# password authentication goes here
		print(password)
		return HttpResponse('HRllo')
	else:
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_profile(request, user_id, format=None):
	"""
	Display specific user information
	"""
	if request.method == 'GET':
		try:
			user = UserProfile.objects.get(pk=user_id)
		except UserProfile.DoesNotExist:
			return Response(status=status.HTTP_404_NO_FOUND)
		serializer = UserProfileSerializer(user)
		return Response(serializer.data)

@api_view(['POST'])
def user_edit(request, user_id, format=None):
	"""
	Update the user profile
	"""
	try:
		user = UserProfile.objects.get(pk=user_id)
	except UserProfile.DoesNotExist:
		return Response(status=status.HTTP_404_NO_FOUND)
	if request.method == 'POST':
		serializer =  UserProfileSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def admin_all(request, format=None):
	"""
	Return all the created user to the admin
	"""
	users = UserProfile.objects.all()
	if request.method == 'GET':
		serializer = UserProfileSerializer(users, many=True)
		return Response(serializer.data)

@api_view(['DELETE'])
def admin_del(request, user_id, format=None):
	"""
	Delete specified user
	"""
	try:
		user = UserProfile.objects.get(pk=user_id)
	except UserProfile.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'DELETE':
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def admin_update(request, user_id, format=None):
	"""
	Update the user profile
	"""
	try:
		user = UserProfile.objects.get(pk=user_id)
	except UserProfile.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = UserProfileSerializer(user)
		return Response(serializer.data)
	if request.method == 'POST':
		serializer =  UserProfileSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
