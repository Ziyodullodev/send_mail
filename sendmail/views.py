from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send(request):
    if request.method == "POST":
        title = request.POST.get('title')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(
            title,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        return render(request, 'index.html', {"action":"seccess"})
    
    return render(request, 'index.html')