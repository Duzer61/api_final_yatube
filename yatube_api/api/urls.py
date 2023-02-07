from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet, basename='comments')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]
