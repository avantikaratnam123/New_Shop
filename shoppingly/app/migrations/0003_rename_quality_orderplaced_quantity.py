# Generated by Django 4.1.7 on 2023-08-05 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_quality_cart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='quality',
            new_name='quantity',
        ),
    ]
