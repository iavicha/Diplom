from django.urls import path
from . import views

urlpatterns = [
    path('', views.objects_index, name='objects_index'),
    path('objects_list', views.objects_list, name='objects_list'),
    path('objects_edit', views.objects_edit, name='objects_edit'),
    path('objects_new', views.objects_new, name='objects_new'),
]