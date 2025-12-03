from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_account = User.objects.create_user(username=username, email=email, password=password)
        user_account.save()
        return redirect("/signin")
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/task")
        else:
            return redirect("/signin")
    return render(request, 'signin.html')

def task(request):
    return render(request, 'task.html')