from django.db import models


# Create your models here.


class Job(models.Model):
    name_job = models.CharField(max_length=250)
    nex_job = models.CharField(max_length=250)
    date_start_job = models.DateField()
    date_end_job = models.DateField()


