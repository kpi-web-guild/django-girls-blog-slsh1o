"""Forms for the blog app."""
from django import forms

from .models import Post


MAX_TITLE_LENGTH = 64


class PostForm(forms.ModelForm):
    """New Post creation form."""

    class Meta:
        """Meta configs for Post form."""

        model = Post
        fields = ['title', 'text']

    def clean_title(self):
        """Control length of title of the post."""
        title = self.cleaned_data.get('title')
        if len(title) >= MAX_TITLE_LENGTH:
            raise forms.ValidationError('Title is too long')
        return title
