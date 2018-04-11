from django.db import models
from django.contrib.auth.models import AbstractUser
from languages import languages



class User(AbstractUser):
	"""
	A customized user model to make 
	email field required and unique.
	"""
	email = models.EmailField(('email address'), unique=True)


class Profile(models.Model):
	"""
	Profile model to save default settings for 
	snippets for each user.
	"""
	LANGUAGES = languages
	EXPOSURE = (
		('public','Public'),
		('private','Private'),
	)

	user = models.OneToOneField(User, related_name='profile')
	default_syntax = models.CharField(max_length=50, choices=LANGUAGES, default='none')
	default_exposure = models.CharField(max_length=20, choices=EXPOSURE, default='public')


	def __str__(self):
		return self.user.username

