from django.urls import path, include 
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), 
    path('', include(router.urls)),
    path('api_auth', views.obtain_auth_token, name='api_auth')
]