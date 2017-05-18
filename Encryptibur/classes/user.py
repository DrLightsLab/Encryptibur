from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    encryptibur_id = models.ForeignKey(Encryptibur, on_delete=models.CASCADE)
