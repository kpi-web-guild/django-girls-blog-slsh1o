"""Views of blog app."""
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def post_list(request):
    """Classic Django posts list view."""
    posts_list = Post.objects \
                     .filter(published_date__lte=timezone.now()) \
                     .order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts_list})


def post_detail(request, post_pk):
    """Classic Django post detail view."""
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    """Classic Django post creation func view."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.published_date = timezone.now()
            obj.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_edit(request, post_pk):
    """Classic Django post edit func view."""
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.published_date = timezone.now()
            obj.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})
