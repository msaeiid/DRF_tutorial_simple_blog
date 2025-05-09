from django.urls import path

from Posts import views

urlpatterns = [
    ##function based view
    path('homepage/', views.homepage, name='homepage'),
    # path('post_list/', views.post_list_add, name='list_post'),
    # path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    # path('post_update/<int:pk>', views.post_update, name='post_update'),
    # path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
    ##class based view
    # path('', views.PostsListView.as_view(), name='posts'),
    # path('<int:pk>', views.PostCreateRetrieveUpdateDeleteView.as_view(), name='post'),
    ## Generic API Views
    path('', views.PostListCreateView.as_view(), name='posts'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='post'),
    path('author/', views.ListPostsForAuthor.as_view(), name='list_posts_for_author'),
]
