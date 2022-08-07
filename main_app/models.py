from django.db import models
from django.urls import reverse

# Create your models here.
SNACKS = (
  ('B', 'Beer'),
  ('S', 'Soda'),
  ('H', 'Hot Dog'),
  ('N', 'Nachos')
)

class Stadium(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("stadiums_detail", kwargs={"stadium_id": self.id})

class Concession(models.Model):
  date = models.DateField('Purchase Date')
  snack = models.CharField(
    max_length=1,
    choices=SNACKS,
    default=SNACKS[0][0]
    )
  stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_snack_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

