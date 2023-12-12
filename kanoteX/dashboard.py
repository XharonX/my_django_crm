from django.views.generic import FormView
from django.shortcuts import render



def kanotex(request):
    return render(request, 'base/new-base.html',)