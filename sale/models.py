from django.db import models
from productions.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.


class SaleChannel(models.Model):
    ...


class Shop(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    location = models.CharField(_('location') ,max_length=255 )
    town = models.CharField(_('town'), max_length=244)
    type = models.CharField(_('type'), help_text='eg. phone accessories', max_length=100)
    popular = models.SmallIntegerField(_('popular'))

    def __str__(self):
        return str(self.name) + ' at ' + str(self.location)


class SaleProduct(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(_('customer name'), max_length=140)
    phone = models.CharField(_('phone number'), max_length=12)
    email = models.EmailField(_('email address'), max_length=255, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        self.warrantycard


class WarrantyCard(models.Model):
    product = models.OneToOneField(SaleProduct, on_delete=models.SET_NULL, null=True)
    is_valid = models.BooleanField(_("validate"), default=False)
    is_invalid = models.BooleanField(_('invalidate'), default=False)
    reason_of_invalid = models.TextField(blank=True)

    def invalid_warranty(self):
        '''
        change valid warranty to invalid warranty
        self.invalid will be true
        self.reason_of_invalid will be modified.
        :return: None
        '''

    def create_warranty(self):
        ...

    def __str__(self):
        info = str(self.saleproduct.customer) + str(self.saleproduct.phone)
        return info


class VoucherSlip(models.Model):
    ...
