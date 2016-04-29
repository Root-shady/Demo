from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	SEXES = (('F', "female"), ('M', "Male"), ('', "======="))
	sex = models.CharField(max_length=1, choices=SEXES, blank=True, default='')
	image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return self.username

class FileManager(models.Model):
	owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	path = models.FileField(upload_to='files/%Y/%m/%d/')

	def __str__(self):
		return str(self.id)
