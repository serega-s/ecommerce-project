# Generated by Django 3.2.5 on 2021-07-17 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20210716_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
