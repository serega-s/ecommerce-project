# Generated by Django 3.2.5 on 2021-07-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_remove_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax_price',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='last_name',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
