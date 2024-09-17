from django.shortcuts import render , redirect
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User 
from .models import hosp , inventory , blood
# Create your views here.

def home(request):
    hospi = hosp.objects.all()
    page = "user"
    context = {"page" : page , 'hospital' : hospi}
    return render(request , "beds/front.html" , context)

def admin_home(request):
    inven = inventory.objects.filter(host = request.user)
    bb = blood.objects.filter(host = request.user)
    hospi = hosp.objects.all()
    page = "admin"
    context = {'page':page , 'hospital' : hospi , 'inven' : inven , 'bb' : bb}
    return render(request , 'beds/dosti.html' , context)

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request , "User does not exist")
        user1 = authenticate(request , username = username , password = password)
        if user1 is not None:
            if user1.is_staff:
                login(request , user1)
                return redirect("hospital-admin")
            login(request , user1)
            return redirect('home')
        else:
            messages.error(request , "User does not Exist")

    context = {'page' : page}
    return render(request , 'beds/login1.html' , context)

def registerPage(request):
    page = "signup"
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , 'An Error Occurred during Registration!')

    context = {'form' : form , 'page':page}
    return render(request , "beds/login1.html" , context)

def adminRegister(request):
    page = "signup"
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_staff = True
            user.save()
            login(request , user)
            return redirect('hospital-admin')
        else:
            messages.error(request , 'An Error Occurred during Registration!')

    context = {'form' : form , 'page':page}

    return render(request , "beds/admin.html" , context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def admin_site(request):
    return render(request , "beds/admin.html")

def next(request , pk):
    hospi = hosp.objects.get(id = pk)
    inven = inventory.objects.filter(host = hospi.host)
    bb = blood.objects.filter(host = hospi.host)
    page = "inside"
    context = {'page' : page , 'hospital' : hospi , 'inven':inven , 'bb':bb} 
    return render(request , 'beds/f3.html' , context)