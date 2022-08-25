from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from datetime import date
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='author', blank=True, null=True, on_delete=models.CASCADE)
    training_name = models.CharField(default=None, max_length=200)
    created_date = models.DateField(default=date.today)

    def __str__(self):
        return self.training_name

    class Meta:
        verbose_name = 'Training'


class Exercise(models.Model):
    tr_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    exercise = models.CharField(default=None, max_length=100)
    sets_count = models.PositiveIntegerField(default=0)
    reps_count = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    exercise_tonnage = models.IntegerField(default=0)

    def __str__(self):
        return self.exercise

    def tonnage(self):
        return self.sets_count * self.reps_count * self.weight

    def save(self, *args, **kwargs):
        self.exercise_tonnage = self.tonnage()
        super(Exercise, self).save(*args, **kwargs)


class Note(models.Model):
    note_author = models.ForeignKey(User, related_name='note_author', blank=True, null=True, on_delete=models.CASCADE)
    note_text = models.TextField(default=None)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.note_text


# function for forming the way to save the photo
def upload_file_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.photo_author, filename)


class Photo(models.Model):
    photo_author = models.ForeignKey(User, related_name='photo_author', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(default=None, max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    im_photo = models.ImageField(upload_to=upload_file_path)

    # image_data is used to display the preview in the admin panel
    def image_data(self):
        return format_html('<img src="{}" width="50px"/>', self.im_photo.url)

    def __str__(self):
        return self.title
