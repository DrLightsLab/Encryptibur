from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Encryptibur(models.Model):
    user = model.ForeignKey(User, on_delete=models.CASCADE)
    category = model.CharField(max_length=30)
    account_name = model.CharField(max_length=30)
    encrypted_value = model.CharField(max_length=50)
    encrypted_length = model.CharField(max_length=10)
