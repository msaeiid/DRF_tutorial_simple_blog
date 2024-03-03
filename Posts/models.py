from django.contrib.auth import get_user_model
from django.db import models

from simpleBlog.settings import AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
