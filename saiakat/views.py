from django.shortcuts import render
from .models import Destinations

# Create your views here.
def home(request):
    dest1 = Destinations()
    dest1.name = "Yssyk Kul"
    dest1.desc = 'Lake of wonders'
    dest1.img = 'img-1.jpg'
    dest1.price = 230
    dest1.offer = True

    dest2 = Destinations()
    dest2.name = 'Naryn'
    dest2.desc = 'Root of Kyrgyzstan'
    dest2.img = 'img-2.jpg'
    dest2.price = 200
    dest2.offer = False

    dest3 = Destinations()
    dest3.name = 'Osh'
    dest3.desc = 'Second capital'
    dest3.img = 'img-3.jpg'
    dest3.price = 280
    dest3.offer = False

    dest4 = Destinations()
    dest4.name = "Batken"
    dest4.desc = 'Another culture'
    dest4.img = 'img-4.jpg'
    dest4.price = 290
    dest4.offer = False

    dest5 = Destinations()
    dest5.name = 'Talas'
    dest5.desc = 'Pride of Kyrgyzstan'
    dest5.img = 'img-5.jpg'
    dest5.price = 190
    dest5.offer = True

    dest6 = Destinations()
    dest6.name = 'Jalal Abad'
    dest6.desc = 'Wanna see nature'
    dest6.img = 'img-6.jpg'
    dest6.price = 310
    dest6.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]
    return render(request,'index.html', {'dests':dests})

def contact(request):
    return render(request,'contact.html')

def myhome(request):
    return render(request, 'home.html')
