from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='index'),
    path('Weabout/', aboutWeView, name='aboutWe'),
]