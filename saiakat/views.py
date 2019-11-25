from django.shortcuts import render
from .models import Destinations, News

# Create your views here.
def home(request):
    dests= Destinations.objects.all()
    news = News.objects.all()
    context = {'dests':dests, 'news':news}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def myhome(request):
    return render(request, 'home.html')
