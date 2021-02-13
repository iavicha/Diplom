from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def aocr_edit(request):
    return render(request, 'aocr/aocr_edit.html')


@login_required
def aocr_list(request):
    return render(request, 'aocr/aocr_list.html')


@login_required
def aocr_all(request):
    return render(request, 'aocr/aocr_list_all.html')
