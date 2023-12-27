from django.contrib.auth.models import AbstractUser, Permission, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Employee(AbstractUser):
    email = models.EmailField(_('email'), max_length=255, unique=True)
    dept = models.ForeignKey('Department', related_name='department', on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey('Position', related_name='position', on_delete=models.SET_NULL, null=True)
    # salary = models.IntegerField(_('salary'), blank=True, null=True, default=0)
    # phone = models.CharField(_('phone'), max_length=12, blank=True)
    # gender = models.CharField(_('gender'), max_length=20, choices=(('male', 'male'), ('female', 'female'), ('none', 'none')), blank=True, default=None)
    # age = models.IntegerField(_('age'), blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Department(models.Model):
    name = models.CharField(_('dept'), max_length=100, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(_('position'), max_length=100)
    # permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


# class Profile(models.Model):
#     user = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(_('full name'), max_length=200, blank=True)
#     age = models.IntegerField(blank=True)
#     gender = models.CharField(_('gender'), max_length=20, choices=(('male', 'male'),('female', 'female')))
#     phone = models.CharField(_('phone number'), max_length=12, unique=True)
#     address1 = models.CharField(_('permanent address'), max_length=300, blank=False)
#     address2 = models.CharField(_('current address'), max_length=300, blank=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     def read_position(self):
#         return f'{self.position} + {self.dept}'


# @receiver(post_save, sender=Employee)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


class EmployeeManager(BaseUserManager):
    def __init__(self, dept):
        super().__init__()
        self.dept_id = dept

    def get_queryset(self, *args, **kwargs):
        member = super().get_queryset(*args, **kwargs)

        return member.filter(dept__id=self.dept_id)

    # def get_dept(self, value):
    #     if type(value) is str():
    #         if value.isdigit():
    #             return int(value)
    #         else:
    #             dept = Department.objects.get(name=value)
    #             return dept.id


class Technician(Employee):
    objects = EmployeeManager(1)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        proxy = True
        verbose_name = 'Technician'
        # verbose_name_plural = 'Technicians'


class Sale(Employee):
    objects = EmployeeManager(3)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        proxy = True
        verbose_name = 'Sale'


class Accounting(Employee):
    objects = EmployeeManager(2)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        proxy = True
        verbose_name = 'Accounting'


class Audit(Employee):
    objects = EmployeeManager(4)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        proxy = True
        verbose_name = 'Audit'



