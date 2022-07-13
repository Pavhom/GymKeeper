from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('training_name', 'exercise', 'set', 'reps_count', 'weight')
