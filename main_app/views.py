from django.shortcuts import render
from .models import Stadium


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stadiums_index(request):
  stadiums = Stadium.objects.all()
  return render(request, 'stadiums/index.html', {'stadiums':stadiums})

def stadiums_detail(request, stadium_id):
  stadium = Stadium.objects.get(id=stadium_id)
  return render(request, 'stadiums/detail.html', { 'stadium':stadium })