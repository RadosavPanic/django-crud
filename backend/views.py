from django.shortcuts import render, redirect

def home(request):
    return render(request, 'signup.html')

def signup(request):
    # if request.method == "POST":
    #     fnm =
    return render(request, 'signup.html')