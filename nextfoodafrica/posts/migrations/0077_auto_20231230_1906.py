# Generated by Django 3.1.4 on 2023-12-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0076_auto_20231230_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
        migrations.AddField(
            model_name='message',
            name='dateMessage',
            field=models.CharField(default='', max_length=100),
        ),
    ]
