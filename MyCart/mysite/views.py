from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .models import User


# Create your views here.

def home(request):
    return render(request,"home.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data.get('name')
            # address = form.cleaned_data.get('address')
            # email = form.cleaned_data.get('email')
            # u = User(name = name, address = address, email = email)
            # u.save()
            # subject = "Message from MyZon.com"
            # message = "%s" %(username)
            # emailFrom = form.cleaned_data.get('email')
            # emailTo = [settings.EMAIL_HOST_USER]
            
            # send_mail(subject,message,emailFrom,emailTo,fail_silently=False)
            # user = authenticate(username = username, password = password)
            # login(request, user)
            return redirect('home')
    else:
        form = SignUpForm

    return render(request, 'signup.html',{'form':form})

def AboutUs(request):
    return render(request,"AboutUS.html")

