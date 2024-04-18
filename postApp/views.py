from django.shortcuts import render
from django.conf import settings
import os

def homeView(request):
    
    current_url = request.path
    print(current_url)
    return render(request, 'index.html', {'current_url': current_url})
