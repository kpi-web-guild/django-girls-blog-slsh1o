"""Views of blog app."""
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def post_list(request, *args, **kwargs):
    """Pure Django REST API posts list view."""
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts_list})


def post_detail(request, post_pk, *args, **kwargs):
    """Pure Django post detail view."""
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'blog/post_detail.htlm', {'post': post})


@login_required
def post_create(request, *args, **kwargs):
    """Classic Django post creation func view."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            obj.published_date = timezone.now()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_edit(request, post_pk, *args, **kwargs):
    """Classic Django post edit func view."""
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            obj.published_date = timezone.now()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})


def post_list_json(request, *args, **kwargs):
    """Pure Django REST API posts list view."""
    query_set = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts_list = [post.serialize() for post in query_set]
    data = {
        'response': posts_list
    }
    return JsonResponse(data)


def post_detail_json(request, post_pk, *args, **kwargs):
    """Pure Django REST API post detail view."""
    data = {
        'post_id': post_pk
    }
    status = 200
    try:
        post = Post.objects.get(pk=post_pk)
        data['author'] = post.author
        data['title'] = post.title
        data['text'] = post.text
        data['created_date'] = post.created_date
        data['published_date'] = post.published_date
    except Post.DoesNotExist:
        data['message'] = 'Post not found'
        status = 404
    return JsonResponse(data, status=status)
