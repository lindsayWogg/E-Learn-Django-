# Generated by Django 3.1.4 on 2024-02-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0091_auto_20240203_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='formation_type',
            field=models.CharField(default='gratuit', max_length=100),
        ),
    ]
