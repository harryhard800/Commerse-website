# Generated by Django 3.2.2 on 2021-05-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210523_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address_line_2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=100),
        ),
    ]