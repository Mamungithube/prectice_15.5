from django.contrib import admin
from django.urls import path
from musician import views
from . import views
urlpatterns = [
    path('', views.add_Album, name='add_Album'),
     path('edit/<int:id>', views.edit, name='edit'),
     path('delete/<int:id>', views.delete, name='delete'),
]