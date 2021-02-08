from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_index, name='material_index'),
    path('material_list', views.material_list, name='material_list'),
    path('material_edit', views.material_edit, name='material_edit'),
]