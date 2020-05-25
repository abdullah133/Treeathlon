# Generated by Django 2.2.9 on 2020-05-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_post_side'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='def', max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='side',
        ),
    ]
