from django.db import models

# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)

class News(models.Model):
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'News/pics')

