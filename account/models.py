from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
	
	def create_user(self, username, email, password, **other_fields):
		if not username:
			raise ValueError('Username required.')
		if not email:
			raise ValueError('Email address required.')
		if not password:
			raise ValueError('Password required.')
		
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, **other_fields)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, username, email, password, **other_fields):
		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser', True)
		return self.create_user(username, email, password, **other_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=254, unique=True)
	email = models.EmailField(max_length=254, unique=True)
	
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]
	
	objects = AccountManager()
	
	class Meta:
		verbose_name = 'Accounts'
		verbose_name_plural = 'Accounts'
	
	def __str__(self):
		return self.username
