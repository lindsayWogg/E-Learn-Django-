# Generated by Django 3.0.12 on 2024-04-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0132_paiement_matricule'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiement',
            name='montant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='paiement',
            name='remarque',
            field=models.TextField(default='AUCUNE', max_length=500),
        ),
    ]