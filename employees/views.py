from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.generic import View, CreateView
from django.http.response import HttpResponseNotAllowed, HttpResponseForbidden
from django.contrib import messages


# Create your views here.


class EmployeeLoginView(View):
   template_name = 'auth/login.html'
   form_class = LoginForm
   success_url = reverse_lazy('desktop')

   def get(self, request, *args, **kwargs):
      if request.user.is_anonymous:
         return render(request, self.template_name, {'form': self.form_class})
      else:
         return HttpResponseForbidden(
            '<h1>405 Your are allowed this page.</h1>'
         )

   def post(self, request, *args, **kwargs):
      if request.user.is_anonymous:
         username = request.POST.get('username')
         password = request.POST.get('password')
         print(username, password)
         account = authenticate(request, username=username, password=password)
         if account is not None:
            print('Authentication Failed.')
            login(request, account)
            return redirect(self.success_url)
         else:
            print('Failed Authentication')
            messages.error(request, 'Failed Authentication')
            return redirect(request.META.get("HTTP_REFERER"))

      else:
         print("U are already login.")
         return redirect(request.META.get("HTTP_REFERER"))


class EmployeeCreateView(CreateView):
   template_name = 'auth/register.html'
   form_class = EmployeeCreationForm
   success_url = reverse_lazy('desktop')

   def post(self, request, *args, **kwargs):
      form = self.form_class(request.POST)
      if form.is_valid():
         fst = form.cleaned_data['first_name']
         lst = form.cleaned_data['last_name']
         username = form.cleaned_data['username']
         email = form.cleaned_data['email']
         dept = form.cleaned_data['dept']
         pos = form.cleaned_data['position']
         password = form.cleaned_data['password']

         try:
            emp = Employee(first_name=fst, last_name=lst, username=username, email=email, dept=dept, \
                           position=pos, is_staff=True)
            emp.set_password(password)
            emp.save()

         except ValueError:
            return "Cannot Create an employee staff."

         return redirect('desktop')
