# Generated by Django 2.2.3 on 2019-08-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_auto_20190830_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='year',
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='questions',
            name='level',
            field=models.IntegerField(default=2),
        ),
    ]