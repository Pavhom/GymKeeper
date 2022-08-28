from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, TemplateView, ListView
from django.contrib.auth.views import LoginView, auth_logout, login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Exercise, Note, Photo
from .forms import PostForm, ExerciseForm, RegisterUserForm, NoteForm, AddPhotoForm
from django.db.models import Sum
from django.core.paginator import Paginator

import calendar
from datetime import datetime


def get_page_context(queryset, request):
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page


@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user).order_by('created_date')[::-1]
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect(post_list)
    else:
        form = PostForm()
    return render(request, 'mainscreen/post_list.html', {'posts': posts,
                                                         'form': form,
                                                         'page': get_page_context(posts, request)})


def notes_list(request):
    notes = Note.objects.filter(note_author=request.user).order_by('created_date')[::-1]
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.note_author = request.user
            form.save()
            return redirect(notes_list)
    else:
        form = NoteForm()
    return render(request, 'mainscreen/notes.html', {'notes': notes,
                                                     'form': form,
                                                     'page': get_page_context(notes, request)})


def photo(request):
    photos = Photo.objects.filter(photo_author=request.user).order_by('created_date')[::-1]
    if request.method == "POST":
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.photo_author = request.user
            form.save()
            return redirect(photo)
    else:
        form = AddPhotoForm()
    return render(request, 'mainscreen/photo.html', {'photos': photos,
                                                     'form': form})


def training_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    exercise = Exercise.objects.filter(tr_post=pk)
    total_tonnage = exercise.aggregate(Sum('exercise_tonnage'))['exercise_tonnage__sum']
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.tr_post = post
            form.save()
            return redirect(training_detail, pk)
    else:
        form = ExerciseForm()
    return render(request, 'mainscreen/training_detail.html', {'post': post,
                                                               'exercise': exercise,
                                                               'form': form,
                                                               'total_tonnage': total_tonnage})


class Chart(TemplateView):
    template_name = 'mainscreen/chart.html'

    # def get_context_data(self, **kwargs):
    #     c = calendar.TextCalendar()
    #     context = super().get_context_data(**kwargs)
    #     context['html_out'] = c.itermonthdays(datetime.today().year, datetime.today().month)
    #     return context


class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'mainscreen/note_edit.html'
    success_url = reverse_lazy('notes_list')


class TrainingDelete(DeleteView):
    model = Post
    template_name = 'mainscreen/delete.html'
    success_url = reverse_lazy('post_list')


class ExerciseDelete(DeleteView):
    model = Exercise
    success_url = '/'
    template_name = 'mainscreen/exercise_delete.html'


class NoteDelete(DeleteView):
    model = Note
    template_name = 'mainscreen/note_delete.html'
    success_url = reverse_lazy('notes_list')


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'mainscreen/photo_delete.html'
    success_url = reverse_lazy('photo')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainscreen/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'mainscreen/login.html'


def logout_user(request):
    auth_logout(request)
    return redirect('login')
