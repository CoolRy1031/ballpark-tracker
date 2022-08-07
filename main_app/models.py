from django.db import models
from django.urls import reverse

# Create your models here.
class Stadium(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("stadiums_detail", kwargs={"stadium_id": self.id})
  