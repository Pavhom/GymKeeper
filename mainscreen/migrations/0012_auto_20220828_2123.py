# Generated by Django 3.2.14 on 2022-08-28 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0011_chart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chart',
            old_name='chart_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='photo_author',
            new_name='author',
        ),
    ]
