from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from datetime import date
from .models import Post, Exercise
from .forms import PostForm, ExerciseForm
# Create your views here.


def post_list(request):
    # display of all workouts
    posts = Post.objects.filter(created_date__lte=date.today()).order_by('-created_date')

    # the next part is responsible for pagination
    paginator = Paginator(posts, 5)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    # need add 'page': page to dict, and use {% include "mainscreen/pagination.html" with page=posts %} after
    # first endfor. Pagination page need only for this func

    # this part is responsible for adding a new workout
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = date.today()
            post.save()
            return redirect(post_list)
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mainscreen/post_list.html', {'page': page, 'posts': posts, 'form': form})


def training_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    exercise = Exercise.objects.filter(tr_post=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.tr_post = post
            form.save()
            return redirect(training_detail, pk)
    else:
        form = ExerciseForm()
    return render(request, 'mainscreen/training_detail.html', {'post': post, 'exercise': exercise, 'form': form})


# def add_training(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.created_date = date.today()
#             post.save()
#             # return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'mainscreen/post_list.html', {'form': form})
