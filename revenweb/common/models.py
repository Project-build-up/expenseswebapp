from django.db import models

# Create your models here.
class Signdata(models.Model):
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=16)
#class Logindata(models.Model):

    