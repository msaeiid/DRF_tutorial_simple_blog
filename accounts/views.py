from django.contrib.auth import authenticate
from rest_framework import generics, status, views
from rest_framework.request import Request
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    model = User

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            content = {
                'auth_token': user.auth_token.key
            }
            return Response(data=content, status=status.HTTP_200_OK)
        else:
            content = {
                'message': 'Invalid username or password'
            }
            return Response(data=content, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        content = {
            'username': str(request.user),
            'auth_token': str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)
