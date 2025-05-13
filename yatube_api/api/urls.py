from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from .views import (
    FollowViewSet, PostViewSet, CustomTokenRefreshView,
    GroupViewSet, UserViewSet, CommentViewSet,
    CustomTokenVerifyView
)


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('users', UserViewSet, basename='users')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='jwt-create'
    ),
    path(
        'v1/jwt/refresh/',
        CustomTokenRefreshView.as_view(),
        name='jwt-refresh'
    ),
    path(
        'v1/jwt/verify/',
        CustomTokenVerifyView.as_view(),
        name='jwt-refresh'
    ),
]
