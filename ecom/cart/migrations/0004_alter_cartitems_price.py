# Generated by Django 5.1.4 on 2024-12-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cartitems_total_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='price',
            field=models.IntegerField(),
        ),
    ]
