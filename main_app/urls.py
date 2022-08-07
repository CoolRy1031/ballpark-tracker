from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('stadiums/', views.stadiums_index, name='stadiums_index'),
  path('stadiums/<int:stadium_id>/', views.stadiums_detail, name='stadiums_detail'),

]