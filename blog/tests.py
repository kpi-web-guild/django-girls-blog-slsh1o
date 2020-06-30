"""Tests for blog app."""
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='testpassword')

    def test_post_created(self):
        post = Post.objects.create(author=self.user, title='Test title', text='Test Text')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, 'Test title')
        self.assertEqual(post.text, 'Test Text')
