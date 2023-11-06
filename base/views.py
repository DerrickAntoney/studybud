from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [{'id': 1, 'name': 'Lets learn python!'},
         {'id': 2, 'name': 'Django Developers'},
         {'id': 3, 'name': 'Lets Design'},
         ]

def home(request):
  context = {'rooms': rooms}
  return render(request, 'home.html', context)

def room(request):
  return render(request, 'room.html')