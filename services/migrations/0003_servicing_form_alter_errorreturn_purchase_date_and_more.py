# Generated by Django 4.2.7 on 2023-11-27 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_errorreturn_code_errorreturn_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicing',
            name='form',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.errorreturn'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='errorreturn',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='errorreturn',
            name='received_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
