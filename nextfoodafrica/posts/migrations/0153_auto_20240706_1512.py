# Generated by Django 3.0.12 on 2024-07-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0152_auto_20240706_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='atelier',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='atelier',
            name='type',
            field=models.CharField(default='17', max_length=200),
        ),
    ]
