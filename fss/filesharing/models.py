from django.db import models

# Create your models here.
# class Operations(models.Model):
#     full_name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30,unique=True)
#     password = models.CharField(max_length=30)

class UserDetails(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    # is_verified = models.BooleanField(default=False)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

