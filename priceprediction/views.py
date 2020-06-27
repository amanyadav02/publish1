from django.shortcuts import render,HttpResponse,redirect
from priceprediction.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def index(request):
   
    return render(request,'priceprediction/index.html')
def about(request):
    return render(request,'priceprediction/about.html')

def services(request):
    return render(request,'priceprediction/services.html')
def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        textarea=request.POST.get('textarea')
        contact=Contact(name=name,email=email,phone=phone,textarea=textarea)
        contact.save()
        messages.success(request,'your message has been sent')
    return render(request,'priceprediction/contact.html')

