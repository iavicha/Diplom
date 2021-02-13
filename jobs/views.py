from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job
from django.http import HttpResponse


# Create your views here.

@login_required
def job_new(request):
    return render(request, 'jobs/job_new.html')


@login_required
def jobs_lists(request):
    return render(request, 'jobs/job_all.html')


@login_required
def job_add(request):
    if request.method == 'POST':
        job_new = request.POST['new_job']
        job_next = request.POST['next_job']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        first_date = start_date.replace('-', '')
        second_date = end_date.replace('-', '')
        first_date, second_date = int(first_date), int(second_date)
        if second_date > first_date:
            result = Job(name_job=job_new, nex_job=job_next,
                         date_start_job=start_date, date_end_job=end_date)
            result.save()
            return redirect('job_new')
        else:
            return redirect('logout')
    elif request.method == 'GET':
        return redirect('job_new')
