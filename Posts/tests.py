from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class HelloWorldTestCase(APITestCase):
    def test_hello_word(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Hello World!")


USER_CREDENTIAL = {
    "password": "77002783",
    "email": "admin@gmail.com",
    "username": "admin"
}


class PostListCreateTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def authenticate(self):
        self.client.post(reverse('signup'), USER_CREDENTIAL)
        USER_CREDENTIAL.pop('username')
        response = self.client.post(reverse('token_obtain_pair'), USER_CREDENTIAL)

        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_list_posts(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation(self):
        self.authenticate()

        sample_data = {
            "title": "sample title",
            "content": "sample content",
            "author": User.objects.get(email=USER_CREDENTIAL['email']).id
        }
        response = self.client.post(reverse('posts'), sample_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], sample_data['title'])
        self.assertEqual(response.data['content'], sample_data['content'])
        self.assertEqual(response.data['author'], User.objects.get(email=USER_CREDENTIAL['email']).id)
