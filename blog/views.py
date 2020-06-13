"""Views of blog app."""
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Post


def post_list(request, *args, **kwargs):
    """Pure Django REST API posts list view."""
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts_list})


def post_detail(request, post_pk, *args, **kwargs):
    """Pure Django post detail view."""
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'blog/post_detail.htlm', {'post': post})
