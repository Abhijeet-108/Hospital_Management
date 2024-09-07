from django.shortcuts import render
from django.http import HttpResponse
#import pandas as pd

# Create your views here.

def home(request):
#    ex = pd.read_csv("C:\Users\Asus\OneDrive\Desktop\stock1.csv")
    context = {'page': 'Home'}
    return render(request , 'beds/front.html', context)

def tery(request):
    return render(request , "main.html")
