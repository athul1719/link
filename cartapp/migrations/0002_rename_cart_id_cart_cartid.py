# Generated by Django 4.2.7 on 2023-12-08 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_id',
            new_name='cartid',
        ),
    ]