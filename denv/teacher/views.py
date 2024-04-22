from django.shortcuts import render, HttpResponse
from .models import Blood_group, Info
from .forms import BloodForm, InfoForm

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
   form = InfoForm()
   if request.method == 'POST' :
      if 'save' in request.POST :
         pk = request.POST.get('save')
         if pk :
            info = Info.objects.get(id = pk)
            form = InfoForm(request.POST, instance=info)
         else :
            form = InfoForm(request.POST)
         form.save()
         form = InfoForm()
      elif 'delete' in request.POST :
         pk = request.POST.get('delete')
         info = Info.objects.get(id = pk)
         info.delete()
      elif 'edit' in request.POST :
         pk = request.POST.get('edit')
         info = Info.objects.get(id = pk)
         form = InfoForm(instance=info)
   context['form'] = form
   return render(request, 'info.html', context)

def blood(request) :
   context = {}
   context['title'] = 'BG page'
   blood = Blood_group.objects.all()
   context['blood'] = blood
   form = BloodForm()
   if request.method == 'POST' :
      if 'save' in request.POST :
         pk = request.POST.get('save')
         if pk :
            blood = Blood_group.objects.get(id = pk)
            form = BloodForm(request.POST, instance=blood)
         else :
            form = BloodForm(request.POST)
         form.save()
         form = BloodForm()
      elif 'delete' in request.POST :
         pk = request.POST.get('delete')
         blood = Blood_group.objects.get(id = pk)
         blood.delete()
      elif 'edit' in request.POST :
         pk = request.POST.get('edit')
         blood = Blood_group.objects.get(id = pk)
         form = BloodForm(instance=blood)
   context['form'] = form
   return render(request, 'blood.html', context)

