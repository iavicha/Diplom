from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal_index, name='journal_index'),
    path('journal_list', views.journal_list, name='journal_list'),
    path('journal_edit', views.journal_edit, name='journal_edit'),
]