# Generated by Django 2.2.9 on 2020-04-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_backgroundimgdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundimgdescription',
            name='content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='backgroundimgdescription',
            name='content3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='backgroundimgdescription',
            name='title2',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='backgroundimgdescription',
            name='title3',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
