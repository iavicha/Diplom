from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def schema_edit(request):
    return render(request, 'schema/schemas_edit.html')


@login_required
def schema_list(request):
    return render(request, 'schema/schemas_list.html')


@login_required
def schema_index(request):
    return render(request, 'schema/schemas.html')

@login_required
def schema_new(request):
    return render(request, 'schema/schemas_new.html')
