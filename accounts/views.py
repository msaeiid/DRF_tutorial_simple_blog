from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, views
from rest_framework.request import Request
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import SignupSerializer
from accounts.tokens import create_jwt_pair_for_user


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    model = User

    @swagger_auto_schema(operation_summary="Create a new user",
                         operation_description="Create a new user by passing information")
    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    @swagger_auto_schema(operation_summary="Authenticate user",
                         operation_description="Authenticate a new user by passing information")
    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            content = {
                'tokens': tokens
            }
            return Response(data=content, status=status.HTTP_200_OK)
        else:
            content = {
                'message': 'Invalid username or password'
            }
            return Response(data=content, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Generate JWT token",
                         operation_description="Generate logged in JWT token")
    def get(self, request: Request):
        tokens = create_jwt_pair_for_user(request.user)
        content = {
            'tokens': tokens
        }
        return Response(data=content, status=status.HTTP_200_OK)
