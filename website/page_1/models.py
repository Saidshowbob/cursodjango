from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=300)
    message = models.TextField()