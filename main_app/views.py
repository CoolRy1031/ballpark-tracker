from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stadium
from .forms import ConcessionForm


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
  concession_form = ConcessionForm()
  return render(request, 'stadiums/detail.html', { 'stadium':stadium, 'concession_form': concession_form })

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

def add_concession(request, stadium_id):
  form = ConcessionForm(request.POST)
  if form.is_valid():
    new_concession= form.save(commit=False)
    new_concession.stadium_id = stadium_id
    new_concession.save()
  return redirect('stadiums_detail', stadium_id=stadium_id)