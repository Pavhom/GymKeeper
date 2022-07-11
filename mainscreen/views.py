from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mainscreen/post_list.html', {'posts': posts})

def training_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mainscreen/training_detail.html', {'post': post})