# Generated by Django 3.0.8 on 2020-07-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200717_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
