# Generated by Django 2.0.1 on 2019-08-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LILO',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='login_time',
            field=models.DateTimeField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='logout_time',
            field=models.DateTimeField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='score1',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='questions',
            name='score2',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='questions',
            name='score3',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='questions',
            name='temp1_Ans',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questions',
            name='temp2_Ans',
            field=models.CharField(default='', max_length=100),
        ),
    ]
