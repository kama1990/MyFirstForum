from django.shortcuts import render

# Create your views here.

def home(required):
    return render(required, 'home.html')