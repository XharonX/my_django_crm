from django.db import models
from employees.models import Sale, Service
from django.dispatch import receiver
from django.db.models.signals import post_save
from productions.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.


class ErrorResult(models.TextChoices):
    ...


class chargedby(models.TextChoices):
    customer = ('cust', 'Customer')
    company = ('comp', 'Company')


class ErrorReturn(models.Model):
    customer = models.CharField('customer name', max_length=255, )
    purchase_date = models.DateTimeField(auto_now_add=False, auto_created=False)
    purchase_shop = models.CharField('shop', max_length=100)
    product = models.ForeignKey(Product, max_length=30, on_delete=models.SET_NULL, null=True)
    qty = models.SmallIntegerField('qty')
    accessories = models.CharField(max_length=300)
    physical_dmg = models.CharField('Physical Damage', max_length=255)
    reason = models.TextField()
    # how_happen = models.TextField(verbose_name=_('How to happen?'), )
    # received_by = models.ManyToManyField(Sale)
    received_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_code + " -> "+ self.reason


class Servicing(models.Model):
    # service_technician = models.ForeignKey(Service, on_delete=models.SET_NULL)
    form = models.OneToOneField(ErrorReturn, on_delete=models.CASCADE)
    technician_finding = models.TextField()
    checked = models.DateTimeField(auto_now=True)
    final_result = models.CharField(max_length=200, choices=ErrorResult.choices)
    fees = models.IntegerField(default=0)
    fees_by = models.CharField(_('charged_by'), max_length=40, choices=chargedby.choices, default=chargedby.company)
    # is_checked = models.BooleanField('finished', default=False, blank=True)

    def __str__(self):
        return self.form.__str__() + self.form.received_date.strftime(" %d-%m-%y")


@receiver(post_save, sender=ErrorReturn)
def created_or_updated_servicing(sender, instance, created, **kwargs):
    if created:
        Servicing.objects.create(form=instance)

    else:
        instance.servicing.form = instance
        instance.servicing.save()