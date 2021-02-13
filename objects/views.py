from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def objects_edit(request):
    return render(request, 'objects/object_edit.html')


@login_required
def objects_list(request):
    return render(request, 'objects/objects_all.html')


@login_required
def objects_index(request):
    return render(request, 'objects/object.html')


@login_required
def objects_new(request):
    return render(request, 'objects/objects_new.html')
