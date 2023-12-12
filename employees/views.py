from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseNotAllowed, HttpResponseForbidden
# Create your views here.


class EmployeeLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return render(request, self.template_name, {'form': self.form_class})
        else:
            return HttpResponseForbidden(
                '<h1>405 Your are allowed this page.</h1>'
            )

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            form = self.form_class(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                print(username, password)
                account = authenticate(request, username=username, password=password)
                if account is not None:
                    login(request, account)
                    return redirect(self.success_url)
            else:
                print(form.errors)
                return redirect(request.META.get("HTTP_REFERER"))
