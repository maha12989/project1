from django.shortcuts import render, HttpResponse
from .models import Blood_group, Info

# Create your views here.
def index(request) :
   context = {}
   context['title'] = 'Home page'
   return render(request, 'index.html', context)

def about(request) :
   context = {}
   context['title'] = 'About page'
   return render(request, 'about.html', context)

def info(request) :
   context = {}
   context['title'] = 'Info page'
   info = Info.objects.all()
   context['info'] = info
   return render(request, 'info.html', context)

def blood(request) :
   context = {}
   context['title'] = 'BG page'
   blood = Blood_group.objects.all()
   context['blood'] = blood
   return render(request, 'blood.html', context)

