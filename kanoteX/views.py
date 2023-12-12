from django.views.generic import FormView
from django.shortcuts import render, redirect




def dashboard(request):
    context = {}
    return render(request, 'pages/home.html', context)
