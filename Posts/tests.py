from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .views import PostListCreateView

User = get_user_model()


class HelloWorldTestCase(APITestCase):
    def test_hello_word(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Hello World!")


class PostListCreateTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PostListCreateView.as_view()
        self.url = reverse('posts')
        self.user = User.objects.create(username='test',
                                        email='test@gmail.com',
                                        password='77002783Sas@#')

    def test_list_posts(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation(self):
        test_post_data = {
            "title": "sample title",
            "content": "sample content",
            "author": self.user.id
        }
        request = self.factory.post(self.url, test_post_data)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
