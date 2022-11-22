# Generated by Django 4.1.1 on 2022-11-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluacion', models.CharField(choices=[('malo', 'Bad'), ('normal', 'Normal'), ('bueno', 'Good')], max_length=6)),
                ('mensaje', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Calificación',
                'verbose_name_plural': 'Calificaciones',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiene_experiencia', models.BooleanField(default=None)),
            ],
        ),
    ]
