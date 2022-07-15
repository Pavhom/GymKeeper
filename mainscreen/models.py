from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from django.db.models import F, Sum


class Post(models.Model):
    training_name = models.CharField(max_length=200)
    created_date = models.DateField(default=date.today)

    def publish(self):
        self.created_date = date.today()
        self.save()

    def __str__(self):
        return self.training_name


class Exercise(models.Model):
    tr_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=200)
    sets_count = models.PositiveIntegerField(default=0)
    reps_count = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    # exercise_tonnage = Post.objects.aggregate(total=Sum(F('sets_count') * F('reps_count') * F('weight')))

    def __str__(self):
        return self.exercise