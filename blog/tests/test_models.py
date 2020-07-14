"""Tests for the models of the blog app."""
from datetime import datetime
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from blog.models import Post


TIMEZONE_NOW_MOCK = datetime(
    day=10,
    month=7,
    year=2019,
    tzinfo=timezone.get_current_timezone(),
)


class TestPostModel(TestCase):
    """Tests for Post model."""

    @classmethod
    def setUpTestData(cls):
        """Prepare non-modified data for test methods."""
        User.objects.create(username='test_user')

    def setUp(self):
        """Prepare modified data for test methods."""
        author = User.objects.get(id=1)
        self.test_post = Post.objects.create(
            author=author,
            title='Test title',
            text='Test text.',
        )

    def tearDown(self):
        """Delete data of previous test."""
        self.test_post.delete()

    def test_post_representation(self):
        """Post model represents itself as its title."""
        self.assertEqual(str(self.test_post), self.test_post.title)

    def test_post_publish_method(self):
        """Test publish method to set date correctly."""
        with patch('django.utils.timezone.now') as mock_timezone_now:
            mock_timezone_now.return_value = TIMEZONE_NOW_MOCK
            self.test_post.publish()
            self.assertEqual(self.test_post.published_date, TIMEZONE_NOW_MOCK)
