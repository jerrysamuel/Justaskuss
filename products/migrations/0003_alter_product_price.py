# Generated by Django 4.1.1 on 2022-09-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_screen_resolution_product_battery_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]
