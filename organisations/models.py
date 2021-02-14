from django.db import models

# Create your models here.


class Organisations(models.Model):
    name_organisatin = models.CharField(max_length=400)
    rekvizity = models.CharField(max_length=400)
    address_of_organistion = models.CharField(max_length=400)
    date_start = models.DateField()
    date_end = models.DateField()