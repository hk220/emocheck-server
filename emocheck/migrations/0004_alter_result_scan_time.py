# Generated by Django 3.2.16 on 2023-01-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emocheck', '0003_alter_result_is_infected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='scan_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
