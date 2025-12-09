from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="/signin")
def task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        obj = models.Task(title=title, user=request.user)
        obj.save()        
        return redirect("/task")
    
    res = models.Task.objects.filter(user=request.user).order_by('-srno')
    return render(request, 'task.html', {'res': res})

@login_required(login_url="/signin")
def edit_task(request, srno):
    if request.method == "POST":
        title = request.POST.get("title")
        obj = models.Task.objects.get(srno=srno)
        obj.title = title
        obj.save()        
        return redirect("/task")
    
    obj = models.Task.objects.get(srno=srno)        
    return render(request, 'edit_task.html', {'obj': obj})

@login_required(login_url="/signin")
def delete_task(request, srno):
    obj = models.Task.objects.get(srno=srno)
    obj.delete()
    return redirect("/task")

def signout(request):
    logout(request)
    return redirect("/signin")