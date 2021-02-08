from django.urls import path
from . import views

urlpatterns = [
    path('job_new', views.job_new, name='job_new'),
    path('jobs_list', views.jobs_lists, name='jobs_list'),
]