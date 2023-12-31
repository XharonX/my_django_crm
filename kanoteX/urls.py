"""
URL configuration for kanoteX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees.views import EmployeeLoginView, EmployeeCreateView
from productions.views import ProductViewSet
from django.contrib.auth.views import LogoutView
from employees.views import DashboardView as dashboard
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard.as_view(), name='desktop'),
    # path('profile/', , name='profile'),
    path('service/', include('services.urls'), name='services'),
    path('api/', include('api.urls'), name="api"),
    path('login/', EmployeeLoginView.as_view(), name='login'),
    path('create-new-employee/', EmployeeCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)