# Generated by Django 3.0.12 on 2024-03-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0120_remove_utilisateur_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='date_souscription',
            field=models.DateField(default='2024-03-30'),
        ),
    ]