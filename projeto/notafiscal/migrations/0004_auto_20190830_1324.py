# Generated by Django 2.2.4 on 2019-08-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0003_auto_20190829_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='numero',
            field=models.IntegerField(verbose_name='Número:'),
        ),
    ]
