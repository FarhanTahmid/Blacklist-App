# Generated by Django 4.1 on 2022-08-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Student ID')),
                ('name', models.CharField(max_length=50, verbose_name='Student Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
        ),
    ]
