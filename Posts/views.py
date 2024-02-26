from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


## First
# def homepage(request: HttpRequest):
#     response = {
#         'message': 'Hello World!'
#     }
#     return JsonResponse(response)

@api_view(["GET", "POST"])
def homepage(request: Request):
    if request.method == "GET":
        response = {'message': 'Hello World!'}
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        response = {'message': 'Hello World!', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)


posts_list_json = [
    {"id": 1, "title": "My first post", "content": "This is my first"},
    {"id": 2, "title": "My second post", "content": "This is my second"},
    {"id": 3, "title": "My third post", "content": "This is my third"},
]


@api_view(["GET"])
def list_posts(request: Request):
    if request.method == "GET":
        response = {'posts': posts_list_json}
        return Response(data=response, status=status.HTTP_200_OK)


@api_view(["GET"])
def post_detail(request: Request, pk: int):
    # pk = int(request.query_params['pk'])
    response = None
    for post in posts_list_json:
        if post['id'] == pk:
            response = {'response': post}
    if response is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(data=response, status=status.HTTP_200_OK)
