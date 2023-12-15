from django.db import models
from employees.models import Employee, Technician, Sale
from django.dispatch import receiver
from django.db.models.signals import post_save
from productions.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.


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
    how_happen = models.TextField(verbose_name=_('How to happen?'), blank=True)
    # received_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    received_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def is_expired(self):
        timeDiff = self.received_date - self.purchase_date
        if timeDiff >= self.product.product_warranty:
            return True
        else:
            return False

    def __str__(self):
        return str(self.product) + " -> " + str(self.reason)


class Servicing(models.Model):
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True)
    form = models.OneToOneField(ErrorReturn, on_delete=models.CASCADE)
    technician_finding = models.TextField()
    checked = models.DateTimeField(auto_now=True)
    final_result = models.CharField(max_length=200)
    fees = models.IntegerField(default=0)
    fees_by = models.CharField(_('charged_by'), max_length=40, choices=chargedby.choices, default=chargedby.company)
    is_checked = models.BooleanField('finished', default=False, blank=True)
    approved = models.BooleanField('approved_by', default=False, blank=True)
    is_done = models.BooleanField('finished', default=False, blank=True)

    def __str__(self):
        return self.form.__str__() + self.form.received_date.strftime(" %d-%m-%y")


# class Finished(models.Model):
#     error_return = models.ForeignKey(ErrorReturn, on_delete=models.CASCADE)
#     servicing = models.ForeignKey(Servicing, verbose_name=_('servicing'), on_delete=models.SET_NULL, null=True)
#     finished_date = models.DateTimeField(_('published date'), auto_now=True)
#     done_by = models.ForeignKey(Employee, verbose_name=_('done by'), on_delete=models.SET_NULL, null=True)
#     is_finished = models.BooleanField(default=False, blank=True)

@receiver(post_save, sender=ErrorReturn)
def created_or_updated_servicing(sender, instance, created, **kwargs):
    if created:
        Servicing.objects.create(form=instance)
    else:
        instance.servicing.form = instance
        instance.servicing.save()


# @receiver(post_save, sender=ErrorReturn)
# def created_or_updated_finished(sender, instance, created, **kwargs):
#     if created:
#         if
#         Finished.objects.create(error_return=instance, is_finished=True,)
#     else:
#         instance.servicing.form = instance
#         instance.servicing.save()


