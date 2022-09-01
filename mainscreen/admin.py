from django.contrib import admin
from .models import Post, Exercise, Note, Photo
# Register your models here.

class ExerciseInline(admin.TabularInline):
    """displaying exercises nested in a workout"""
    model = Exercise


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "image_data"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["training_name", "created_date", "author"]
    inlines = [ExerciseInline,]


admin.site.register(Post, PostAdmin)
admin.site.register(Note)
admin.site.register(Photo, ImageAdmin)