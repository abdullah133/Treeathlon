# Generated by Django 2.2.9 on 2020-04-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactadressen',
            name='email',
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
    ]
