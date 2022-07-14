from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(created_date__lte=date.today()).order_by('-created_date')
    paginator = Paginator(posts, 3)  # 3 posts in each page
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
    return render(request, 'mainscreen/post_list.html', {'page': page, 'posts': posts})

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
