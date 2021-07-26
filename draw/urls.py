# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('taskboard/', views.taskboard, name='taskboard'),
    path('phone/', views.phone, name='phone'),
    path('add/', views.add, name='add'),
    path('login/', views.login, name='login'),
    path('<str:room_name>/', views.room, name='room'),

]
