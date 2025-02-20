# comments/views.py
from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsCommentAuthorOrPostAuthorOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCommentAuthorOrPostAuthorOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.all().order_by('-created_at')
        # If nested under posts, use 'post_pk' from the URL kwargs to filter comments for that post.
        post_id = self.kwargs.get('post_pk')
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        # If using nested routes, retrieve the post from the URL.
        post_id = self.kwargs.get('post_pk')
        if post_id:
            serializer.save(user=self.request.user, post_id=post_id)
        else:
            serializer.save(user=self.request.user)
