# Generated by Django 2.2.4 on 2019-08-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0004_auto_20190830_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Peso(Kg):'),
        ),
    ]
