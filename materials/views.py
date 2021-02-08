from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def material_edit(request):
    return render(request, 'materials/material_edit.html')


@login_required
def material_list(request):
    return render(request, 'materials/materials_all.html')


@login_required
def material_index(request):
    return render(request, 'materials/materials.html')
