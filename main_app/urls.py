from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('stadiums/', views.stadiums_index, name='stadiums_index'),
  path('stadiums/<int:stadium_id>/', views.stadiums_detail, name='stadiums_detail'),
  path('stadiums/create/', views.StadiumCreate.as_view(), name='stadiums_create'),
  path('stadiums/<int:pk>/update/', views.StadiumUpdate.as_view(), name='stadiums_update'),
  path('stadiums/<int:pk>/delete/', views.StadiumDelete.as_view(), name='stadiums_delete'),
  path('stadiums/<int:stadium_id>/add_concession/', views.add_concession, name='add_concession'),
  path('accounts/signup/', views.signup, name='signup'),

]