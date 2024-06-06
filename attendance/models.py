# from django.db import models

# class Contact(models.Model):
#     email = models.CharField(max_length=100)
#     name = models.CharField(max_length=20)
# # Create your models here.

from django.db import models

class ContactUs(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
