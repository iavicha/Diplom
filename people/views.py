from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def people_edit(request):
    return render(request, 'people/people_edit.html')


@login_required
def people_list(request):
    return render(request, 'people/people_list.html')


@login_required
def people_index(request):
    return render(request, 'people/people.html')
