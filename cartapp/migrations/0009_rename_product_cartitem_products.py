# Generated by Django 4.2.7 on 2023-12-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0008_rename_carts_cartitem_cart_alter_cartitem_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='products',
        ),
    ]
