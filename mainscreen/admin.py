from django.contrib import admin
from .models import Post, Exercise, Note, Photo
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo_author", "image_data"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["training_name", "created_date", "author"]

admin.site.register(Exercise)
admin.site.register(Post, PostAdmin)
admin.site.register(Note)
admin.site.register(Photo, ImageAdmin)