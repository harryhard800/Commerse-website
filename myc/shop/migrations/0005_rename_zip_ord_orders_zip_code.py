# Generated by Django 3.2.2 on 2021-05-23 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='zip_ord',
            new_name='zip_code',
        ),
    ]