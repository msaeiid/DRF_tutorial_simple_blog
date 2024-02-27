from rest_framework import serializers

from Posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)

    class Meta:
        model = Post
        fields = '__all__'
