# Generated by Django 2.2.3 on 2019-08-28 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190829_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='attempt1',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='attempt2',
        ),
    ]
