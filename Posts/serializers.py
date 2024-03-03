from rest_framework import serializers

from Posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', ]
