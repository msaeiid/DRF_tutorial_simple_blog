from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import views, generics, mixins, status, viewsets

from Posts.models import Post
from Posts.permissions import ReadOnly, IsOwnerOrReadOnly
from Posts.serializers import PostSerializer

User = get_user_model()


## function based views

@api_view(["GET", "POST"])
@permission_classes([permissions.AllowAny, ])
def homepage(request: Request):
    if request.method == "GET":
        response = {'message': 'Hello World!'}
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        response = {'message': 'Hello World!', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    # @api_view(http_method_names=["GET", "POST"])
    # def post_list_add(request: Request):
    #     if request.method == "GET":
    #         posts = Post.objects.all()
    #         serializers = PostSerializer(instance=posts, many=True)
    #         response = {'message': 'posts...', 'data': serializers.data}
    #         return Response(data=response, status=status.HTTP_200_OK)
    #     if request.method == "POST":
    #         data = request.data
    #         serializer = PostSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             response = {'message': 'post created', 'data': serializer.data}
    #             return Response(data=response, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(["GET"])
    # def post_detail(request: Request, pk: int):
    #     post = get_object_or_404(Post, id=pk)
    #     serializer = PostSerializer(instance=post)
    #     response = {'message': 'requested post is :', 'data': serializer.data}
    #     return Response(data=response, status=status.HTTP_200_OK)
    #
    #
    # @api_view(http_method_names=['PUT'])
    # def post_update(request: Request, pk: int):
    #     post = get_object_or_404(Post, id=pk)
    #     serializer = PostSerializer(data=request.data, instance=post)
    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {'message': 'Post updated successfully', 'data': serializer.data}
    #     return Response(data=response, status=status.HTTP_200_OK)
    #
    #
    # @api_view(http_method_names=['DELETE'])
    # def post_delete(request: Request, pk: int):
    #     post = get_object_or_404(Post, id=pk)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    ## class based views
    # class PostListCreateView(views.APIView):
    #     serializer_class = PostSerializer
    #     model = Post
    #
    #     def get(self, request: Request, *args, **kwargs):
    #         posts = self.model.objects.all()
    #         serializer = self.serializer_class(posts, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     def post(self, request: Request, *args, **kwargs):
    #         serializer = self.serializer_class(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #
    #
    # class PostCreateRetrieveUpdateDeleteView(views.APIView):
    #     serializer_class = PostSerializer
    #     model = Post
    #
    #     def get(self, request: Request, *args, **kwargs):
    #         post = get_object_or_404(self.model, id=kwargs.get('pk'))
    #         serializer = self.serializer_class(post, many=False)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    #     def put(self, request: Request, *args, **kwargs):
    #         post = get_object_or_404(self.model, id=kwargs.get('pk'))
    #         serializer = self.serializer_class(post, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status.HTTP_200_OK)
    #         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #
    #     def delete(self, request: Request, *args, **kwargs):
    #         get_object_or_404(self.model, id=kwargs.get('pk')).delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    ## Generic API Views and mixins


class PostListCreateView(generics.ListCreateAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    serializer_class = PostSerializer
    model = Post
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        request.data['author'] = request.user.pk
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


## viewsets and routers -> ViewSet

# class PostViewset(viewsets.ViewSet):
#     model = Post
#     serializer_class = PostSerializer
#
#     def list(self, request: Request):
#         posts = self.model.objects.all()
#         serializer = self.serializer_class(instance=posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.model, pk=pk)
#         serializer = self.serializer_class(instance=post, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)


## viewsets and routers -> ModelViewSet
# class PostViewset(viewsets.ModelViewSet):
#     model = Post
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     permission_classes = [IsOwnerOrReadOnly, ]


class CustomPagination(PageNumberPagination):
    page_size = 3
    # request for more object on each page
    page_size_query_param = 'page_size'
    page_query_param = 'page'


# pagination
class ListPostsForAuthor(generics.ListAPIView,
                         mixins.ListModelMixin):
    serializer_class = PostSerializer
    model = Post
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        # about query...
        username = self.request.query_params.get('username') or None
        if username:
            return Post.objects.filter(author__username=username)
        return Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
