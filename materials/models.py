from django.db import models


# Create your models here.


class Materials(models):
    material_name = models.CharField(max_length=400)
    how_nuch = models.IntegerField()
    ed_izm = models.CharField(max_length=4)
    sert_name = models.CharField(max_length=400)
    sert_date_1 = models.DateField()
    sert_date_2 = models.DateField()
    sert_file = models.FileField()
    sanp_name = models.CharField(max_length=400)
    sanp_date_1 = models.DateField()
    sanp_date_2 = models.DateField()
    sanp_file = models.FileField()
    passport_name = models.CharField(max_length=400)
    passport_date = models.DateField()
    passport_file = models.FileField()
    pozhar_name = models.CharField(max_length=400)
    pozhar_date_1 = models.DateField()
    pozhar_date_2 = models.DateField()
    pozhar_file = models.FileField()
