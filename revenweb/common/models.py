from django.db import models

# Create your models here.
class Income(models.Model):
    income=models.CharField(max_length=100)
    amount=models.IntegerField(null=True)
class Expense(models.Model):
    expense=models.CharField(max_length=100)
    spent=models.IntegerField(null=True)