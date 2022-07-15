from django import forms
from .models import Post
from django.forms import TextInput, NumberInput, ModelForm
from .models import Exercise


class ExerciseForm(ModelForm):

    class Meta:
        model = Exercise
        fields = ('exercise', 'sets_count', 'reps_count', 'weight')


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('training_name', 'created_date')

        # widgets = {
        #     "exercise": TextInput(attrs={'placeholder': 'Exercise'}),
        #     "sets_count": NumberInput(attrs={'placeholder': 'Sets count'}),
        #     "reps_count": NumberInput(attrs={'placeholder': 'Reps count'}),
        #     "weight": NumberInput(attrs={'placeholder': 'Weight'}),
        # }

