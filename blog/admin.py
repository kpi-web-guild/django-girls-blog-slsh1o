"""Configs for admin of blog app."""
from django.contrib import admin
from .models import Post


admin.site.register(Post)
