# Generated by Django 4.1.1 on 2022-11-25 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0004_alter_cursos_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tiene_experiencia',
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
        migrations.CreateModel(
            name='Profile_Experiencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PrimeraApp.experiencias')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PrimeraApp.profile')),
            ],
        ),
    ]
