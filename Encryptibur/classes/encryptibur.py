from django.db import models

class Encryptibur(models.Models):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	account = models.charField(max_length=100)
	value = models.charField(max_length=200)
	
