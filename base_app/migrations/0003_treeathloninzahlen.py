# Generated by Django 2.2.9 on 2020-04-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20200425_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeathlonInZahlen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('spenden_number', models.IntegerField()),
            ],
        ),
    ]