# Generated by Django 5.0.4 on 2024-04-24 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_coupon_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='COUPON',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
