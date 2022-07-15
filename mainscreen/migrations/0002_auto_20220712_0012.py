# Generated by Django 3.2.14 on 2022-07-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='exercise',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='reps_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='set',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='training_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
