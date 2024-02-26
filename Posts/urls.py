from django.urls import path

from Posts import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('list_posts/', views.list_posts, name='list_posts'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
]
