from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html', {'name' : 'Esen'})

def add(request):
    first = request.POST['numb1']
    second = request.POST['numb2']
    ress= int(first)+int(second)
    return render(request,'result.html',{'result':ress})
