from django.db import models


# Create your models here.


class Product(models.Model):
    warranty = list()
    for m in range(8):
        warranty.append((m, str(m)+' months'))
    product_code = models.CharField('code', max_length=20, unique=True, primary_key=True)
    product_name = models.CharField("Product Name", max_length=255, unique=True)
    product_price = models.IntegerField('price')
    product_warranty = models.IntegerField('warranty months', choices=warranty)

    def __str__(self):
        return self.product_code


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    label = models.CharField('Enter the label of specification: ', max_length=50)
    value = models.CharField('Enter the value of the specification: ', max_length=100)

    def __str__(self):
        return str(self.product) + 'specification'


class Barcode(models.Model):
    ...

