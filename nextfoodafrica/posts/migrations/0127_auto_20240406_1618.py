# Generated by Django 3.0.12 on 2024-04-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0126_auto_20240406_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande_inscription',
            name='formation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.formation'),
        ),
    ]
