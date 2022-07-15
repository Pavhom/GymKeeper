# Generated by Django 3.2.14 on 2022-07-14 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0012_auto_20220715_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=200)),
                ('sets_count', models.PositiveIntegerField(default=0)),
                ('reps_count', models.PositiveIntegerField(default=0)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('tr_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainscreen.post')),
            ],
        ),
    ]
