from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

@login_required
def job_new(request):
    return render(request, 'jobs/job_new.html')


@login_required
def jobs_lists(request):
    return render(request, 'jobs/job_all.html')
