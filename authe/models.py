from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class registermodel(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    dob=models.DateField()
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=10, choices=li)
    