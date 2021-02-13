from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_index, name='people_index'),
    path('people_list', views.people_list, name='people_list'),
    path('people_edit', views.people_edit, name='people_edit'),
]