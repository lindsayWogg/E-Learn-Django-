# Generated by Django 3.0.12 on 2024-04-06 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0131_paiement'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiement',
            name='matricule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.utilisateur'),
        ),
    ]