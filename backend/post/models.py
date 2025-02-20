from django.db import models
from useraccounts.models import CustomUser  # Ensure correct import

class Post(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(
        CustomUser,
        related_name='liked_posts',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add this field for tracking updates

    def __str__(self):
        return self.title
