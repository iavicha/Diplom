from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Materials


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


@login_required
def add_material(request):
    if request.method == "POST":
        material_name = request.POST['material_name']
        how_nuch = request.POST['how_nuch']
        ed_izm = request.POST['ed_izm']
        sert_name = request.POST['sert_name']
        sert_date_1 = request.POST['sert_date_1']
        sert_date_2 = request.POST['sert_date_2']
        sert_file = request.POST['sert_file']
        sanp_name = request.POST['sanp_name']
        sanp_date_1 = request.POST['sanp_date_1']
        sanp_date_2 = request.POST['sanp_date_2']
        sanp_file = request.POST['sanp_file']
        passport_name = request.POST['passport_name']
        passport_date = request.POST['passport_date']
        passport_file = request.POST['passport_file']
        pozhar_name = request.POST['pozhar_name']
        pozhar_date_1 = request.POST['pozhar_date_1']
        pozhar_date_2 = request.POST['pozhar_date_2']
        pozhar_file = request.POST['pozhar_file']
        result = Materials(material_name=material_name,how_nuch=how_nuch,ed_izm=ed_izm,sert_name=sert_name,
                           sert_date_1=sert_date_1,sert_date_2=sert_date_2, sert_file=sert_file,sanp_name=sanp_name,
                           sanp_date_1=sanp_date_1,sanp_date_2=sanp_date_2,sanp_file=sanp_file,
                           passport_name=passport_name,passport_date=passport_date,passport_file=passport_file,
                           pozhar_name=pozhar_name, pozhar_date_1=pozhar_date_1, pozhar_date_2=pozhar_date_2,
                           pozhar_file=pozhar_file)
        result.save()
        return redirect('material_index')
