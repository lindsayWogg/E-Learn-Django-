# Generated by Django 3.1.4 on 2023-12-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0066_formation'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='foormation_img',
            field=models.CharField(default='', max_length=100),
        ),
    ]
