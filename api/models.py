from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, max_length=200)
    password = models.CharField(blank=False, max_length=200)
    registered_at = models.DateTimeField(auto_now=True)
    