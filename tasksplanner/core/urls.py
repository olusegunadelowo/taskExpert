from django.contrib import admin
from django.urls import path
from .views import base, create,update,delete

urlpatterns = [
    path('', base, name='home'),
    path('create/', create, name='create_task'),
    path('update/<int:int>', update, name='update_task'),
    path('delete/<int:int>', delete, name='delete_task'),
]