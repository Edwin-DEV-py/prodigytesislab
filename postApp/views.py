from django.shortcuts import render
from django.conf import settings
import os

def homeView(request):
    
    return render(request, 'index.html')
