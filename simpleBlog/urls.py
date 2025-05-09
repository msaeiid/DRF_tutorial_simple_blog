"""
URL configuration for simpleBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_view
from Posts import views as posts_views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
# router.register('', posts_views.PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('Posts.urls'), name='homepage'),
    ## viewsets and routers
    # path('post/', include(router.urls)),
    path('auth/', include('accounts.urls')),
    path('auth/create', jwt_view.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', jwt_view.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify', jwt_view.TokenVerifyView.as_view(), name='token_verify'),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Blog API description",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mskarbaschian@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
