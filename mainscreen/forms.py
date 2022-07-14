from django import forms
from .models import Post
from django.forms import TextInput, NumberInput, ModelForm


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('exercise', 'sets_count', 'reps_count', 'weight')

        # widgets = {
        #     "exercise": TextInput(attrs={'placeholder': 'Exercise'}),
        #     "sets_count": NumberInput(attrs={'placeholder': 'Sets count'}),
        #     "reps_count": NumberInput(attrs={'placeholder': 'Reps count'}),
        #     "weight": NumberInput(attrs={'placeholder': 'Weight'}),
        # }

