from django.shortcuts import render
from .models import Destinations

# Create your views here.
def home(request):
    dests= Destinations.objects.all()
    context = {'dests':dests}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def myhome(request):
    return render(request, 'home.html')
