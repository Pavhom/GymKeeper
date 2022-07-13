from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    training_name = models.CharField(max_length=200)
    exercise = models.CharField(max_length=200)
    sets_count = models.PositiveIntegerField(default=0)
    reps_count = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    # def publish(self):
    #     self.created_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.exercise

