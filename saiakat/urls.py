from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'saiakat-home'),
    path('index',views.home, name ='index'),
    path('contact',views.contact, name ='contact'),
    path('myhome',views.myhome, name ='myhome')
]
