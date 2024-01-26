from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from .models import Income,Expense
from django.contrib.auth.models import User,auth
from django.contrib import messages
import csv
import os
from django.conf import settings

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
"""# incomespent--
def incspent(request):
    if request.method=="POST":
        expense1=request.POST.get('expenseName')
        spent1=request.POST.get('expenseAmount')
        incsp=Income.objects.create(expense=expense1,spent=spent1)
        incsp.save()
        messages.info(request,"Spent Successfully Added")
        return redirect(incspent)
    else:
        return render(request,"newexp.html")
# incomeadded--
def incsal(request):
    if request.method=="POST":
        income1=request.POST.get('incomeSource')
        amount1=request.POST.get('incomeAmount')
        incsa=Expense.objects.create(income=income1,amount=amount1)
        incsa.save()
        messages.info(request,"Income Successfully Added")

    else:
        return render(request,"newincome.html")"""
# logout--
def logout(request):
    auth.logout(request)
    return redirect('welcome')
# download report
def download(request):
    return render(request,"rep.html")
def incspent(request):
    if request.method=='POST':
        dict1=request.POST
        with open("static/media/incspent.csv","a") as f1:
            wrt=csv.writer(f1)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    return render(request,"newexp.html")
def incsal(request):
    if request.method=="POST":
        dict1=request.POST
        with open("static/media/incomeadd.csv","a") as f1:
            wrt=csv.writer(f1)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    return render(request,"newincome.html")
def downloadincome(request):
    f1path=os.path.join(settings.BASE_DIR,'static/media/incomeadd.xlsx')
    file=open(f1path,"rb")
    response = FileResponse(file, content_type='text/csv')
    response['downcontent'] = 'attachment; filename="incomeadd.xlsx"'
    return response
def downloadspent(request):
    f1path = os.path.join(settings.BASE_DIR, 'static/media/incspent.xlsx')
    file=open(f1path,'rb')
    response = FileResponse(file, content_type='text/csv')
    response['downcontent'] = 'attachment; filename="incspent.xlsx"'
    return response