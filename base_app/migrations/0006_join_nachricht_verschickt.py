# Generated by Django 2.2 on 2020-05-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_auto_20200427_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='nachricht_verschickt',
            field=models.BooleanField(default=False),
        ),
    ]
