from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    training_name = models.CharField(max_length=200)
    exercise = models.CharField(max_length=200)
    set = models.IntegerField()
    reps_count = models.IntegerField()
    weight = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.exercise
