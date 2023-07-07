from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    workers = models.ManyToManyField(User)

    def __str__(self):
        return self.name
