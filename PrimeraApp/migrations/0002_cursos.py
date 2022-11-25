# Generated by Django 4.1.1 on 2022-11-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=50)),
                ('subtítulo', models.CharField(max_length=150)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]