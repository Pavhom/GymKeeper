from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.views import LoginView, auth_logout, login_required
from django.contrib.auth.forms import AuthenticationForm
from datetime import date
from .models import Post, Exercise
from .forms import PostForm, ExerciseForm, RegisterUserForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def post_list(request):
    # display of all workouts
    posts = Post.objects.filter(author=request.user, created_date__lte=date.today()).order_by('-created_date')
    # this part is responsible for adding a new workout
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_date = date.today()
            post.author = request.user
            post.save()
            return redirect(post_list)
    else:
        form = PostForm()
    return render(request, 'mainscreen/post_list.html', {'posts': posts, 'form': form})


def training_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    exercise = Exercise.objects.filter(tr_post=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # form.post = Post.objects.get(pk=pk)
            form.tr_post = post
            form.save()
            return redirect(training_detail, pk)
    else:
        form = ExerciseForm()
    return render(request, 'mainscreen/training_detail.html', {'post': post, 'exercise': exercise, 'form': form})


class TrainingDelete(DeleteView):
    model = Post
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'mainscreen/delete.html'


class ExerciseDelete(DeleteView):
    model = Exercise
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'mainscreen/exercise_delete.html'


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

