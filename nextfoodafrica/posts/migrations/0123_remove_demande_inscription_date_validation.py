# Generated by Django 3.0.12 on 2024-03-30 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0122_demande_inscription_date_validation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande_inscription',
            name='date_validation',
        ),
    ]
