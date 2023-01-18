from django.db import models

# Create your models here.
"""class Eventos(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)"""


class Eventos(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()
  TYPE_CHOICES = (
    ('F', 'Familiar'),
    ('T', 'Trabajo'),
  )
  type = models.CharField(max_length=1, choices=TYPE_CHOICES)
  description = models.TextField()
