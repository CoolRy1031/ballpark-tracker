from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stadium
from .forms import ConcessionForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def stadiums_index(request):
  stadiums = Stadium.objects.filter(user=request.user)
  return render(request, 'stadiums/index.html', {'stadiums':stadiums})

@login_required
def stadiums_detail(request, stadium_id):
  stadium = Stadium.objects.get(id=stadium_id)
  concession_form = ConcessionForm()
  return render(request, 'stadiums/detail.html', { 'stadium':stadium, 'concession_form': concession_form })

class StadiumCreate(LoginRequiredMixin, CreateView):
  model = Stadium
  fields = ['name', 'location', 'description']
  success_url = '/stadiums/'

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class StadiumUpdate(LoginRequiredMixin, UpdateView):
  model = Stadium
  fields = ['description', 'location']

class StadiumDelete(LoginRequiredMixin, DeleteView):
  model = Stadium
  success_url = '/stadiums/'

@login_required
def add_concession(request, stadium_id):
  form = ConcessionForm(request.POST)
  if form.is_valid():
    new_concession= form.save(commit=False)
    new_concession.stadium_id = stadium_id
    new_concession.save()
  return redirect('stadiums_detail', stadium_id=stadium_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('stadiums_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)