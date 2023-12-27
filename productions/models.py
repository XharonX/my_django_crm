from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    product_code = models.CharField('code', max_length=20, unique=True, primary_key=True)
    product_name = models.CharField("Product Name", max_length=255, unique=True)
    product_price = models.IntegerField('price')
    product_warranty = models.IntegerField('warranty months', choices=[(m * 3, str(m * 3) + ' months') for m in range(1, 8)])

    def __str__(self):
        return f"{str(self.product_code)}"

    def returnProduct(self):
        return f"{str(self.product_code)} ({str(self.product_name)})"


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='spec')
    label = models.CharField('Feature: ', max_length=50)
    value = models.CharField('Feature\'s Value: ', max_length=100)

    def __str__(self):
        return str(self.product) + 'specification'


class Catalog(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=150, blank=True)
    publisher = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

    def __str__(self):
        return self.name


class CatalogCategory(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='catalog', on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', related_name='category', on_delete=models.SET_NULL, null=True, blank=True, )
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)

    def __str__(self):
        if self.parent:
            return '{}:\t{}  -  {} '.format(self.catalog.name, self.parent.name, self.name)
        return '{}:\t{} '.format(self.catalog.name, self.name)


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Promotion(models.Model):
    title = models.CharField(_('promotion title'), max_length=100, )
    items = models.ManyToManyField(Product)
    start_date = models.DateTimeField(auto_created=True)
    end_date = models.DateTimeField(auto_created=True)
    dis_percent = models.FloatField()
    discount = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.discount == 0.0:
            total = sum(i.price for i in self.items.all())
            avg = total / self.items.count()
            self.discount = avg * (self.dis_percent / 100)
        return super().save(*args, **kwargs)



# class Distribution(models.Model):
#     distributed_date = models.DateTimeField(auto_created=True)
#     items = models.IntegerField('items')
#     requested_by = models.ForeignKey(User, related_name='requested', on_delete=models.SET_NULL, null=True)
#     approved_by = models.ForeignKey(User, related_name='approved', on_delete=models.SET_NULL, null=True)
