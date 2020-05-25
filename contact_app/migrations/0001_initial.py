# Generated by Django 2.2.9 on 2020-04-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAdressen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(default='default', max_length=40)),
                ('telefon', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default', max_length=40)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]