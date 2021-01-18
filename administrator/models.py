from django.db import models


# Create your models here.
class Menus(models.Model):
    name = models.CharField(max_length=8, blank=True)
    route = models.CharField(max_length=100, default='#')
    order = models.IntegerField(default=0)
