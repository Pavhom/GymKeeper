from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from datetime import date
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(created_date__lte=date.today()).order_by('-created_date')
    return render(request, 'mainscreen/post_list.html', {'posts': posts})

def training_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mainscreen/training_detail.html', {'post': post})

def enter(request):
    return render(request, 'mainscreen/enter.html')

def add_training(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = date.today()
            post.save()
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mainscreen/add_training.html', {'form': form})
