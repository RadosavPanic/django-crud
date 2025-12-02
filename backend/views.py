from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models

def home(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Username: {username}, Email: {email}, Password: {password}")
    return render(request, 'signup.html')