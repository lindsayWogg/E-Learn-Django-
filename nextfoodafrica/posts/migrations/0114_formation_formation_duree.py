# Generated by Django 3.0.12 on 2024-03-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0113_auto_20240302_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='formation_duree',
            field=models.CharField(default='UNDEFINED', max_length=300),
        ),
    ]
