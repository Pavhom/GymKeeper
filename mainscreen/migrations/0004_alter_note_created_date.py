# Generated by Django 3.2.14 on 2022-07-23 20:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0003_auto_20220723_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 20, 48, 42, 835810, tzinfo=utc)),
        ),
    ]