# Generated by Django 3.0.12 on 2024-04-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0125_auto_20240330_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande_inscription',
            name='dmd_date',
            field=models.CharField(default='2024-04-06', max_length=100),
        ),
        migrations.AlterField(
            model_name='formation',
            name='created_at',
            field=models.CharField(default='2024-04-06', max_length=100),
        ),
        migrations.AlterField(
            model_name='souscription_formation',
            name='date_souscription',
            field=models.DateField(default='2024-04-06'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='date_souscription',
            field=models.DateField(default='2024-04-06'),
        ),
    ]
