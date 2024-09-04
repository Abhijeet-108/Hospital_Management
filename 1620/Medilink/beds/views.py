from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request , 'beds/front.html')

def tery(request):
    return render(request , "main.html")
