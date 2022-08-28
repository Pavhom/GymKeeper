from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, auth_logout, login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Exercise, Note, Photo, Chart
from .forms import PostForm, ExerciseForm, RegisterUserForm, NoteForm, AddPhotoForm, ChartForm
from django.db.models import Sum
from django.core.paginator import Paginator


def get_page_context(queryset, request):
    """pagination function"""
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page


def form_save(current_form, redct, request):
    """used for saving forms, redirecting after saving, and assigning an author"""
    if request.method == "POST":
        form = current_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect(redct)
    else:
        form = current_form()
        return form


@login_required
def post_list(request):
    """creates workouts and displays a list of them"""
    posts = Post.objects.filter(author=request.user).order_by('created_date')[::-1]
    form = form_save(PostForm, post_list, request)
    context = {'posts': posts, 'form': form, 'page': get_page_context(posts, request),}
    return render(request, 'mainscreen/post_list.html', context)


@login_required
def notes_list(request):
    """creates notes and displays a list of them"""
    notes = Note.objects.filter(author=request.user).order_by('created_date')[::-1]
    form = form_save(NoteForm, notes_list, request)
    context = {'notes': notes, 'form': form, 'page': get_page_context(notes, request),}
    return render(request, 'mainscreen/notes.html', context)


@login_required
def create_chart(request):
    """creates charts and displays a list of them"""
    charts = Chart.objects.filter(author=request.user).order_by('created_date')[::-1]
    form = form_save(ChartForm, create_chart, request)
    context = {'charts': charts, 'form': form,}
    return render(request, 'mainscreen/chart.html', context)


@login_required
def photo(request):
    """upload photos and display them all"""
    photos = Photo.objects.filter(author=request.user).order_by('created_date')[::-1]
    form = form_save(AddPhotoForm, photo, request)
    context = {'photos': photos, 'form': form,}
    return render(request, 'mainscreen/photo.html', context)


@login_required
def training_detail(request, pk):
    """saves and displays exercises within a workout"""
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
    context = {'post': post, 'exercise': exercise, 'form': form, 'total_tonnage': total_tonnage,}
    return render(request, 'mainscreen/training_detail.html', context)


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
