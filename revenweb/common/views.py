from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signdata
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
# Home page--
def welcome(request):
    return render(request,'home.html')

# signup views---

def signup(request):
    if request.method=='POST':
        email=request.POST['useremail']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'E-mail_already_in_Use')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username_already_taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(email=email,username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password mismatched')
            return redirect('signup')
    else:
        return render(request,"signup.html")

# login views---

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentials_Not_Found")
            return redirect('login')
    else:
        return render(request,"login.html")
# incomespent--
def incspent(request):
    return render(request,"income.html")
# incomeadded--
def addexp(request):
    return render(request,"index.html")
# logout--
def logout(request):
    auth.logout(request)
    return redirect('welcome')