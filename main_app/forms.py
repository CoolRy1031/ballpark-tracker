from django.forms import ModelForm
from .models import Concession

class ConcessionForm(ModelForm):
  class Meta:
    model = Concession
    fields = ['date', 'snack']