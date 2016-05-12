from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	SEXES = (('F', "female"), ('M', "Male"), ('', "======="))
	sex = models.CharField(max_length=1, choices=SEXES, blank=True, default='')
	image = models.ImageField(upload_to='users/%Y/%m/%d', default='', null=True)
	is_admin = models.BooleanField(default=False)
	
	@receiver(post_save, sender=settings.AUTH_USER_MODEL)
	def create_auth_token(sender, instance=None, created=False, **kwargs):
		if created:
			Token.objects.create(user=instance)

	def __str__(self):
		return self.username

class FileManager(models.Model):
	owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	path = models.FileField(upload_to='files/%Y/%m/%d/')

	def __str__(self):
		return str(self.id)
