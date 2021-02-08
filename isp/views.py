from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def isp_edit(request):
    return render(request, 'isp/isp_edit.html')


@login_required
def isp_list(request):
    return render(request, 'isp/isp_list.html')


@login_required
def isp_new(request):
    return render(request, 'isp/isp_new.html')

@login_required
def isp_index(request):
    return render(request, 'isp/isp.html')
