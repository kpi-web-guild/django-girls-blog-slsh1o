"""Tests for the forms of the blog app."""
from django.test import TestCase

from blog.forms import PostForm, MAX_TITLE_LENGTH


class TestPostForm(TestCase):
    """Tests for Post form."""

    def test_title_is_too_long(self):
        """Test form isn't valid if title is too long."""
        form = PostForm(
            data={
                'title': 't' * MAX_TITLE_LENGTH,
                'text': 'Text.',
            },
        )
        self.assertFalse(form.is_valid())

    def test_title_max_length(self):
        """Test form is valid if title length fine."""
        form = PostForm(
            data={
                'title': 't' * (MAX_TITLE_LENGTH-1),
                'text': 'Text.',
            },
        )
        self.assertTrue(form.is_valid())
