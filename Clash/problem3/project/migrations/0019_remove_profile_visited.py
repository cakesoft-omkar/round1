# Generated by Django 2.2.3 on 2019-08-29 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20190829_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='visited',
        ),
    ]
