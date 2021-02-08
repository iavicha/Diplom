from django.urls import path
from . import views

urlpatterns = [
    path('', views.isp_index, name='isp_index'),
    path('isp_list', views.isp_list, name='isp_list'),
    path('isp_new', views.isp_new, name='isp_new'),
    path('isp_edit', views.isp_edit, name='isp_edit'),
]
