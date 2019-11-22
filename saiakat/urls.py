from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'saiakat-home'),
    path('index',views.home, name ='saiakat-index'),
    path('contact',views.contact, name ='saiakat-contact'),
    path('myhome',views.myhome, name ='saiakat-myhome')
]
