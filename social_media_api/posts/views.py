from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

'''
Using Django REST Framework’s viewsets, 
set up CRUD operations for both posts and comments in posts/views.py.
Implement permissions to ensure users can only edit or delete their own posts and comments
'''
class CustomPagination(PageNumberPagination):
    page_size = 10  # You can override this in settings.py
    page_size_query_param = 'page_size'
    max_page_size = 100
  
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination  # Enable pagination
    filter_backends = [filters.SearchFilter]  # Enable filtering
    search_fields = ['title', 'content']  # Users can search by title or content

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)    