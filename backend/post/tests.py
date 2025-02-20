from django.test import TestCase
from useraccounts.models import CustomUser  # Fixed import
from post.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        """Set up test data before running tests."""
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123"
        )
        self.another_user = CustomUser.objects.create_user(
            email="john@example.com",
            username="john_doe",
            password="securepass"
        )
        self.post = Post.objects.create(
            user=self.user,
            title="My First Post",
            content="This is the content of my first post!"
        )

    def test_post_creation(self):
        """Test if a post is created successfully."""
        self.assertEqual(self.post.title, "My First Post")
        self.assertEqual(self.post.user, self.user)

    def test_post_likes(self):
        """Test liking a post."""
        self.post.likes.add(self.another_user)  # John likes the post
        self.assertEqual(self.post.likes.count(), 1)
        self.assertIn(self.another_user, self.post.likes.all())

    def test_fetching_user_posts(self):
        """Test fetching all posts by a user."""  # ✅ Fixed indentation
        user_posts = self.user.posts.all()  # ✅ Use `posts` instead of `post_set`
        self.assertEqual(user_posts.count(), 1)
        self.assertEqual(user_posts.first().title, "My First Post")

    def test_fetching_liked_posts(self):
        """Test fetching all posts liked by a user."""  # ✅ Fixed indentation
        self.post.likes.add(self.another_user)
        liked_posts = self.another_user.liked_posts.all()  # ✅ Use `liked_posts`
        self.assertEqual(liked_posts.count(), 1)
        self.assertEqual(liked_posts.first().title, "My First Post")
