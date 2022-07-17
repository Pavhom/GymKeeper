from django import forms
from .models import Post, Exercise
from django.forms import TextInput, ModelForm, PasswordInput, EmailInput, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class': 'form-input'}))
    email = CharField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Repeat password', widget=PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     "username": TextInput(attrs={'class': 'form-input'}),
        #     "email": EmailInput(attrs={'class': 'form-input'}),
        #     "password1": PasswordInput(attrs={'class': 'form-input'}),
        #     "password2": PasswordInput(attrs={'class': 'form-input'}),
        # }