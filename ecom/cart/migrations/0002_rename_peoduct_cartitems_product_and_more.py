# Generated by Django 5.1.4 on 2024-12-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='peoduct',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
    ]
