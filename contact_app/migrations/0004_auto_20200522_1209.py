# Generated by Django 2.2 on 2020-05-22 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0003_auto_20200425_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactadressen',
            options={'verbose_name': 'Contact Info', 'verbose_name_plural': 'Unser Kontakt info auf der Contact Seite'},
        ),
        migrations.AlterModelOptions(
            name='contactusinfo',
            options={'verbose_name': 'Beschreibung', 'verbose_name_plural': 'Unser Kontakt Beschreibung auf der Contact Seite oben'},
        ),
    ]