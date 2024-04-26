from django.shortcuts import render
from django.conf import settings
from .forms import SendEmailForm
import os

#enviar correo
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes


def homeView(request):
    
    form = SendEmailForm()
    current_url = request.path
    
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        
        if form.is_valid():
            
            name = form.cleaned_data['Nombre']
            email = form.cleaned_data['Correo']
            
            urlImagen = request.build_absolute_uri('/static/img/logoB.png')
            
            #arreglarrrr
            page = get_current_site(request)
            mail = 'Confirmación de contacto - PRODIGY'
            body = render_to_string('emails/emailTemplate.html',{
                'user':name,
                'email':email,
                'domain':page,
                'url':urlImagen
            })
            
            send_mail = EmailMessage(
                mail,body,settings.EMAIL_HOST_USER,to=[email]
            )
            send_mail.content_subtype = 'html'
            send_mail.from_email = False
            send_mail.send()
            
            
            form = SendEmailForm()
        
    context = {
        'form':form,
        'current_url': current_url
    }
    
    return render(request, 'index.html', context)

def aboutWeView(request):
    
    current_url = request.path
    return render(request, 'aboutWe.html', {'current_url': current_url})
