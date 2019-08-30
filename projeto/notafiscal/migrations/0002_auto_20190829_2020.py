# Generated by Django 2.2.4 on 2019-08-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='empresa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Empresa:'),
        ),
        migrations.AlterField(
            model_name='notafiscal',
            name='numero',
            field=models.IntegerField(max_length=44, null=True, unique=True, verbose_name='Número:'),
        ),
    ]
