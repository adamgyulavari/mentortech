from django.db import models

# Create your models here.

class Mentor(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'

class Opinion(models.Model):
    mentor      = models.ForeignKey(Mentor)
    name        = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name + ' (' + self.mentor.email + ')'
