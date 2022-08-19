from django import forms
from .models import Post, Exercise, Note, Photo
from django.forms import TextInput, ModelForm, PasswordInput, EmailInput, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ('exercise', 'sets_count', 'reps_count', 'weight')
        widgets = {'exercise': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   'sets_count': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   'reps_count': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   'weight': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('training_name',)
        widgets = {'training_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'})}


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('note_text',)
        widgets = {'note_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})}


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'im_photo')
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                   'im_photo': forms.FileInput(attrs={'class': 'form-control form-control-sm', 'type': 'file'}),
                   }


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class': 'form-input'}))
    email = CharField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Repeat password', widget=PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
