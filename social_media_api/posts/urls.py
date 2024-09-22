from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("", include(router.urls)),
    path('feed/', feed, name='feed'),
    path("<int:pk>/like/", LikePostView.as_view(), name='like_post'),
    path("<int:pk>/unlike/", UnlikePostView.as_view(), name='unlike_post'),
]

