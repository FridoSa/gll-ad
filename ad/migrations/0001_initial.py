# Generated by Django 3.1.2 on 2020-11-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mitarbeiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anrede', models.CharField(choices=[('f', 'Frau'), ('m', 'Herr'), ('d', '*')], default='d', max_length=1)),
                ('vorname', models.CharField(max_length=20)),
                ('nachname', models.CharField(max_length=30)),
                ('nr', models.CharField(blank=True, help_text='Bei gleichen Vor- und Nachnamen', max_length=5)),
                ('adresszusatz', models.CharField(blank=True, max_length=20)),
                ('strasse', models.CharField(max_length=50)),
                ('pLZ', models.SmallIntegerField(max_length=5)),
                ('ort', models.CharField(max_length=20)),
                ('telefon', models.CharField(blank=True, max_length=20)),
                ('handy', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('geboren', models.DateField()),
                ('eintritt', models.DateField()),
                ('austritt', models.DateField(blank=True)),
                ('iBAN', models.CharField(max_length=34)),
                ('bankname', models.CharField(max_length=30)),
                ('art', models.CharField(choices=[('h', 'Helfer*in'), ('a', 'Angestellt'), ('f', 'FSJ')], default='h', max_length=1)),
                ('personenkonto', models.CharField(blank=True, max_length=20)),
                ('stundenlohn', models.CharField(blank=True, max_length=10)),
                ('limit', models.CharField(blank=True, max_length=5, verbose_name='Jahreslimit für Aufwandsentschädigung')),
                ('gesperrt', models.BooleanField(default=False, verbose_name='Verdienstabrechnung gesperrt')),
                ('meldung', models.TextField(blank=True, verbose_name='Meldung bei Verdienstabrechnung')),
                ('notizen', models.TextField(blank=True, verbose_name='AD-Notizen')),
            ],
        ),
    ]
