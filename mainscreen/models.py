from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date


class Post(models.Model):
    training_name = models.CharField(max_length=200)
    created_date = models.DateField(default=date.today)
    exercise = models.CharField(max_length=200)
    sets_count = models.PositiveIntegerField(default=0)
    reps_count = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)


    # def publish(self):
    #     self.created_date = date.today()
    #     self.save()

    def __str__(self):
        return self.exercise
