from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def my_logout(request):
    logout(request)
    return redirect('homepage')