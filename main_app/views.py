from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class StadiumCreate(CreateView):
  model = Stadium
  fields = '__all__'
  success_url = '/stadiums/'

class StadiumUpdate(UpdateView):
  model = Stadium
  fields = ['description', 'location']

class StadiumDelete(DeleteView):
  model = Stadium
  success_url = '/stadiums/'