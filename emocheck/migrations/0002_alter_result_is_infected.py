# Generated by Django 3.2.16 on 2023-01-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emocheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='is_infected',
            field=models.BooleanField(choices=[(True, 'yes'), (False, 'no')]),
        ),
    ]
