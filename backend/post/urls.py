# api/urls.py
from django.urls import path, include
from rest_framework_nested import routers
from post.views import PostViewSet
from comments.views import CommentViewSet

# Main router for posts
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested router for comments under posts
posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]
