# Generated by Django 3.0.12 on 2024-02-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0110_auto_20240229_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre',
            name='chap_order',
            field=models.IntegerField(default=0),
        ),
    ]