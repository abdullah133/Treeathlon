# Generated by Django 2.2.9 on 2020-04-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teilnahme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=100)),
                ('nachname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('alter', models.CharField(max_length=100)),
                ('ergebnis_1', models.CharField(blank=True, max_length=100, null=True)),
                ('ergebnis_2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
