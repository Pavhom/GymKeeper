from django.contrib import admin
from .models import Post, Exercise, Note, Photo
# Register your models here.


class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "im_photo"]


admin.site.register(Exercise)
admin.site.register(Post)
admin.site.register(Note)
admin.site.register(Photo, imageAdmin)