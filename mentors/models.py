from django.db import models

# Create your models here.

class Mentor(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.CharField(max_length=100)
    description = models.TextField()

class Opinion(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
