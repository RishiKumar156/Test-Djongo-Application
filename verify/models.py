from django.db import models

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, db_index=True)
    email = models.EmailField(max_length=150, unique=True, db_index=True, default='example@example.com')
    password = models.CharField(max_length=150)
    create = models.DateField()