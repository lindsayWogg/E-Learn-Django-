# Generated by Django 3.1.4 on 2024-01-20 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0089_auto_20240120_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='firstname',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='lastname',
            new_name='username',
        ),
    ]