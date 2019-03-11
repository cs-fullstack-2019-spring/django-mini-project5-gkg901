from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('allrecipes/', views.allrecipes, name='allrecipes'),
    path('newrecipe/', views.newrecipe, name='newrecipe'),
    path('profile/', views.profile, name='profile'),
    path('newuser/', views.newuser, name='newuser'),
    path('details/<int:ID>', views.details, name='details'),
    path('edituser/<int:ID>', views.edituser, name='edituser'),
    path('editrecipe/<int:ID>', views.editrecipe, name='editrecipe'),
]