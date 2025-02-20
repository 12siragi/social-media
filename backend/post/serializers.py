from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'title', 'content',
            'likes', 'likes_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'likes', 'likes_count', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def create(self, validated_data):
        # Automatically assign the logged-in user as the owner of the post.
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post
