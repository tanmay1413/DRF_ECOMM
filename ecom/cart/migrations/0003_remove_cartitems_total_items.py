# Generated by Django 5.1.4 on 2024-12-28 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_peoduct_cartitems_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='total_items',
        ),
    ]
