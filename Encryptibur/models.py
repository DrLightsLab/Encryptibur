from __future__ import unicode_literals
from django.contrib.auth.models import (User, BaseUserManager, AbstractBaseUser)
from django.contrib.auth.hashers import check_password
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Encryptibur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    account_name = models.CharField(max_length=30)
    encrypted_value = models.CharField(max_length=50)
    encrypted_length = models.CharField(max_length=10)

class EncryptiburBaseUser(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):

        if not email:
            raise ValueError('An Encrptibur user email is required.')

            user = self.model(
                first_name=first_name,
                last_name=last_name,
                email=self.normalize_email(email),
            )
