# Generated by Django 3.1.2 on 2020-11-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitarbeiter',
            name='pLZ',
            field=models.SmallIntegerField(),
        ),
    ]
