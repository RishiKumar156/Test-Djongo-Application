from django.db import models
# Create your models here.
class Register (models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)

class Login(models.Model):
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    