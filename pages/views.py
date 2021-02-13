from django.shortcuts import render


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'pages/index.html')
    else:
        return render(request, 'login/login.html')