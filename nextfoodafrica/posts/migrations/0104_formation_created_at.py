# Generated by Django 3.0.12 on 2024-02-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0103_auto_20240224_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='created_at',
            field=models.CharField(default='2024-02-24', max_length=100),
        ),
    ]
