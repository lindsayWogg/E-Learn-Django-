# Generated by Django 3.1.4 on 2023-12-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0067_formation_foormation_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='bientot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_id', models.IntegerField(default=0)),
                ('prog_title', models.CharField(default='', max_length=100)),
                ('prog_descr', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='formation',
            name='formation_descr',
            field=models.TextField(default=''),
        ),
    ]
