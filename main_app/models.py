from django.db import models
from django.forms import CharField

# Create your models here.
class Stadium(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name