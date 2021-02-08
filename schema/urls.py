from django.urls import path
from . import views

urlpatterns = [
    path('', views.schema_index, name='schema_index'),
    path('schema_list', views.schema_list, name='schema_list'),
    path('schema_edit', views.schema_edit, name='schema_edit'),
    path('schema_new', views.schema_edit, name='schema_new'),
]