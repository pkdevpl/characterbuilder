from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("character:index")
        else:
            return render(request, "user/login.html", {"error_message": "Niepoprawne dane logowania"})
    else:
        return render(request, "user/login.html")

def logout_view(request):
    logout(request)
    return render(request, "user/logout.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        passwordRepeat = request.POST["passwordRepeat"]
        if password != passwordRepeat:
            return render(request, "user/register.html", {"error_message": "Hasła różnią się od siebie"})
        user = User.objects.create_user(username, None, password)
        if user is not None:
            return redirect("character:index")
        else:
            return render(request, "user/login.html", {"error_message": "Coś poszło nie tak"})
    else :
        return render(request, "user/register.html")