# Generated by Django 3.0.12 on 2024-03-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0123_remove_demande_inscription_date_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande_inscription',
            name='date_validation',
            field=models.CharField(default='', max_length=50),
        ),
    ]