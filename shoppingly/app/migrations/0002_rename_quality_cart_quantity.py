# Generated by Django 4.1.7 on 2023-07-21 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quality',
            new_name='quantity',
        ),
    ]
