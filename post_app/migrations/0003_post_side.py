# Generated by Django 2.2.9 on 2020-05-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_auto_20200505_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='side',
            field=models.TextField(default='def'),
        ),
    ]