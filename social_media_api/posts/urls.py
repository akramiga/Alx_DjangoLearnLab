from django.urls import path, include
from rest_framework.routers  import DefaultRouter
from .views import PostViewSet, CommentViewSet
router = DefaultRouter()
router.register( 'my-models', PostViewSet,CommentViewSet)
urlpatterns=[
    path('api/', include(router.urls))
   
  
]