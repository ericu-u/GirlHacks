# Generated by Django 3.2.5 on 2022-03-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20220326_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bmi',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(default='Male', max_length=10),
            preserve_default=False,
        ),
    ]
