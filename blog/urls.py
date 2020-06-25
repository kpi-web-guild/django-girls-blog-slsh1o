"""The blog URL mapping."""
from django.urls import path

from .views import (
    post_list, post_detail,
    post_create, post_edit,
)


urlpatterns = [
    path('', post_list, name='post_list'),
    path('create-post/', post_create, name='post_create'),
    path('post/<int:post_pk>/', post_detail, name='post_detail'),
    path('post/<int:post_pk>/edit/', post_edit, name='post_edit'),
]
