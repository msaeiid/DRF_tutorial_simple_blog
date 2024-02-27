from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from Posts.models import Post
from Posts.serializers import PostSerializer


@api_view(["GET", "POST"])
def homepage(request: Request):
    if request.method == "GET":
        response = {'message': 'Hello World!'}
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        response = {'message': 'Hello World!', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "POST"])
def list_posts(request: Request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializers = PostSerializer(instance=posts, many=True)
        response = {'message': 'posts...', 'data': serializers.data}
        return Response(data=response, status=status.HTTP_200_OK)
    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        response = {'message': 'post created', 'data': serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def post_detail(request: Request, pk: int):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(instance=post)
    response = {'message': 'requested post is :', 'data': serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=['PUT'])
def post_update(request: Request, pk: int):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(data=request.data, instance=post)
    if serializer.is_valid():
        serializer.save()
        response = {'message': 'Post updated successfully', 'data': serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=['DELETE'])
def post_delete(request: Request, pk: int):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
