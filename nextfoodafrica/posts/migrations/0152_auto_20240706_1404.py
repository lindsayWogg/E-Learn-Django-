# Generated by Django 3.0.12 on 2024-07-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0151_auto_20240706_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='atelier',
            name='heure_debut',
            field=models.CharField(default='8', max_length=2),
        ),
        migrations.AddField(
            model_name='atelier',
            name='heure_fin',
            field=models.CharField(default='17', max_length=2),
        ),
        migrations.AddField(
            model_name='atelier',
            name='lieu',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='atelier',
            name='titre',
            field=models.CharField(default='', max_length=500),
        ),
    ]