# Generated by Django 4.1.1 on 2022-11-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0003_profile_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Experiencias',
            new_name='experiencias',
        ),
        migrations.AddField(
            model_name='profile',
            name='tiene_experiencia',
            field=models.BooleanField(default=False),
        ),
    ]
