# Generated by Django 2.2.4 on 2019-08-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notafiscal',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='notafiscal',
            name='empresa',
            field=models.CharField(blank=True, max_length=80, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='notafiscal',
            name='serie',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
