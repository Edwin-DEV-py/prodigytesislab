from django.shortcuts import render
from django.conf import settings
import os

def homeView(request):
    
    current_url = request.path
    return render(request, 'index.html', {'current_url': current_url})

def aboutWeView(request):
    
    current_url = request.path
    return render(request, 'aboutWe.html', {'current_url': current_url})
