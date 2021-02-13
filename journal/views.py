from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def journal_edit(request):
    return render(request, 'journal/journal_edit.html')


@login_required
def journal_list(request):
    return render(request, 'journal/journal_all.html')


@login_required
def journal_index(request):
    return render(request, 'journal/journal.html')
