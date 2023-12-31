# Generated by Django 4.2.7 on 2023-12-13 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('publisher', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='code')),
                ('product_name', models.CharField(max_length=255, unique=True, verbose_name='Product Name')),
                ('product_price', models.IntegerField(verbose_name='price')),
                ('product_warranty', models.IntegerField(choices=[(3, '3 months'), (6, '6 months'), (9, '9 months'), (12, '12 months'), (15, '15 months'), (18, '18 months'), (21, '21 months')], verbose_name='warranty months')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Feature: ')),
                ('value', models.CharField(max_length=100, verbose_name="Feature's Value: ")),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='productions.product')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField(auto_created=True)),
                ('start_date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='promotion title')),
                ('dis_percent', models.FloatField()),
                ('discount', models.FloatField(default=0.0)),
                ('items', models.ManyToManyField(to='productions.product')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productions.product')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=150)),
                ('catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='catalog', to='productions.catalog')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='productions.catalogcategory')),
            ],
        ),
    ]
