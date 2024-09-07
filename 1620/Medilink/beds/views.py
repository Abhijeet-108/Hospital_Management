from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
#import pandas as pd

# Create your views here.

def home(request):
#    ex = pd.read_csv("C:\Users\Asus\OneDrive\Desktop\stock1.csv")
    context = {'page': 'Home'}
    return render(request , 'beds/front.html', context)

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request , "User Does not Exists")
        user1 = authenticate(request , username = username , password = password)
        if user1 is not None:
            login(request , user1)
            return redirect("home")
        else:
            messages.error(request , "User Does not exist")
    context = {'page' : page}
    return render(request , "beds/login1.html" , context)

def registerPage(request):
    page = "signup"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request , user)
            return redirect("home")
        else:
            messages.error(request , "Enter correct Details")
    context = {'form':form}
    return render(request , "beds/login1.html" , context)

def logoutPage(request):
    logout(request)
    return redirect("home")