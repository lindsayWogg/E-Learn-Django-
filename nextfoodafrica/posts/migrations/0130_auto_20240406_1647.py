# Generated by Django 3.0.12 on 2024-04-06 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0129_auto_20240406_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demande_inscription',
            old_name='matricule_user',
            new_name='matricule',
        ),
    ]