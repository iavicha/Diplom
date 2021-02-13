from django.urls import path
from . import views


urlpatterns = [
    path('aocr_page', views.aocr_edit, name='aocr_new'),
    path('aocr_list', views.aocr_list, name='aocr_list'),
    path('aocr_all', views.aocr_all, name='aocr_all'),
]
