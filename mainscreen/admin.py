from django.contrib import admin
from .models import Post, Exercise, Note
# Register your models here.


admin.site.register(Exercise)
admin.site.register(Post)
admin.site.register(Note)