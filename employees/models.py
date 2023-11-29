from .usermanagements import UserManager
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class JBType(models.TextChoices):
    freelance = 'Freelance', 'freelance'
    path_time = 'Part Time', 'pt'
    full_time = 'Full Time' 'ft'


class Position(models.TextChoices):
    executive = '1', "Executive"
    manager = '2', 'Manager'
    supervisor = '3', 'Sale'
    admin = '4', 'Admin'
    staff = '5', 'Staff'


class Department(models.TextChoices):
    sale = 'Sale', 'sale'
    tech = 'Technician' 'technician'
    service = 'Service', 'service'
    marketing = 'Maketing', 'marketing'
    general = "General", 'gen'
    audit = 'Audit', 'audit'
    finance = 'Finance', 'finance'
    research = 'Research', 'research'
    wh = 'Warehouse', 'wh'
    hr = 'HR', 'hr'


class User(AbstractUser):
    name = models.CharField(_('name'), max_length=150, null=True)
    department = models.CharField(_('department'), max_length=20, choices=Department.choices)
    position = models.CharField(_('position'), max_length=20, choices=Position.choices)
    salary = models.IntegerField(null=True)
    aboutme = models.TextField(blank=True)
    objects = UserManager()

    def __str__(self):
        msg = f"{self.email}, {self.department}, {self.position}"
        if self.position is "BOD" and self.username is "kanoteBOD":
            msg += f"password: kanotex"
        return f"{self.username}, {self.department}, {self.position}"


class SaleDept(UserManager):
    def get_queryset(self, *args, **kwargs):
        rst = super().get_queryset(*args, **kwargs)
        return rst.filter(department=Department.choices.sale)


class Sale(User):
    objects = SaleDept
    
    def welcome(self):
        return f"Welcome to join with us. \n Hello {self.username}"

    def email(self):
        ...

    class Meta:
        proxy = True
        verbose_name = 'Sale'
        verbose_name_plural = "Sales"


class TechDept(UserManager):
    def get_queryset(self, *args, **kwargs):
        rst = super().get_queryset(*args, **kwargs)
        return rst.filter(department=Department.choices.tech)


class Technician(User):
    objects = TechDept

    class Meta:
        proxy = True
        verbose_name = 'Technician'
        verbose_name_plural = 'Technicians'


class ServiceDept(UserManager):
    def get_queryset(self, *args, **kwargs):
        rst = super().get_queryset(*args, **kwargs)
        return rst.filter(department=Department.choices.service)


class Service(User):
    objects = ServiceDept

    class Meta:
        proxy = True
        verbose_name='Service'
        verbose_name_plural = "Services"


class FinanceDept(UserManager):
    def get_queryset(self, *args, **kwargs):
        rst = super().get_queryset(*args, **kwargs)
        return rst.filter(department=Department.choices.service)


class Finance(User):
    objects = FinanceDept

    class Meta:
        proxy = True


class WHDept(UserManager):
    def get_queryset(self, *args, **kwargs):
        rst = super().get_queryset(*args, **kwargs)
        return rst.filter(department=Department.choices.wh)


class Warehouse(User):
    objects = WHDept

    class Meta:
        proxy = True


class AuditDept(UserManager):
    def get_queryset(self, *args, **kwargs):
        rst = super().get_queryset(*args, **kwargs)
        return rst.filter(department=Department.choices.audit)


class Audit(User):
    objects = AuditDept

    class Meta:
        proxy = True
