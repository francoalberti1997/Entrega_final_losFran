# Generated by Django 4.1.1 on 2022-11-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0002_cursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
