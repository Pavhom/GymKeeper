from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'mainscreen/post_list.html', {'posts': posts})

def training_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mainscreen/training_detail.html', {'post': post})

def enter(request):
    return render(request, 'mainscreen/enter.html')

def add_training(request):
    form = PostForm()
    return render(request, 'mainscreen/add_training.html', {'form': form})