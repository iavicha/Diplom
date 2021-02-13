from django.db import models


# Create your models here.


class Materials(models.Model):
    material_name = models.CharField(max_length=400)
    how_nuch = models.IntegerField(null=True, blank=True)
    ed_izm = models.CharField(max_length=4, null=True)
    sert_name = models.CharField(max_length=400, null=True)
    sert_date_1 = models.DateField(null=True)
    sert_date_2 = models.DateField(null=True)
    sert_file = models.FileField(null=True)
    sanp_name = models.CharField(max_length=400,null=True)
    sanp_date_1 = models.DateField(null=True)
    sanp_date_2 = models.DateField(null=True)
    sanp_file = models.FileField(null=True)
    passport_name = models.CharField(max_length=400,null=True)
    passport_date = models.DateField(null=True)
    passport_file = models.FileField(null=True)
    pozhar_name = models.CharField(max_length=400,null=True)
    pozhar_date_1 = models.DateField(null=True)
    pozhar_date_2 = models.DateField(null=True)
    pozhar_file = models.FileField(null=True)

