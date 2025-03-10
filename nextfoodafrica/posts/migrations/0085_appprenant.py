# Generated by Django 3.1.4 on 2024-01-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0084_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='appprenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('sex', models.CharField(default='', max_length=100)),
                ('date_birth', models.DateField(default='')),
                ('picture', models.CharField(default='', max_length=100)),
                ('date_member', models.DateField(default='')),
                ('post', models.CharField(default='', max_length=100)),
                ('nationality', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('userName', models.CharField(default='', max_length=100)),
                ('passWord', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
