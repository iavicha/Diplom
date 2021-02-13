from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Вход выполнен')
            return redirect('index')
        else:
            messages.error(request, 'Вход не выполнен')
            return redirect('login')
    else:
        return render(request, 'login/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login/login.html')