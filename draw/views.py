# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def test(request):
    return render(request, 'draw/test.html')

def taskboard(request):
    return render(request, 'draw/taskboard.html')

def phone(request):
    return render(request, 'draw/phone.html')

def add(request):
    return render(request, 'draw/add.html')

def login(request):
    return render(request, 'draw/login.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
