# Generated by Django 3.0.12 on 2024-02-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0100_chapitre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapitre',
            name='description',
            field=models.TextField(default='Descripioin du chapitre ...'),
        ),
    ]
