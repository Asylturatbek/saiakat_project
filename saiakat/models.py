from django.db import models

# Create your models here.
class Destinations:
    id: str
    name: str
    img: str
    desc: str
    price: int
    offer: bool
