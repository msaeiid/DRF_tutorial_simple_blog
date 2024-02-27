from django.urls import path

from Posts import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('list_posts/', views.list_posts, name='list_posts'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('post_update/<int:pk>', views.post_update, name='post_update'),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
]
