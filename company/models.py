from django.db import models
from worker.models import Worker

class Company(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    workers = models.ManyToManyField(
        to=Worker,
        blank=True,
        related_name='company'
    )
    def __str__(self):
        return self.name
