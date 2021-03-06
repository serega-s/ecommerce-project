# Generated by Django 3.2.5 on 2021-08-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0030_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
