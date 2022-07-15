# Generated by Django 3.2.14 on 2022-07-13 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0004_rename_set_post_sets_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reps_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='sets_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
