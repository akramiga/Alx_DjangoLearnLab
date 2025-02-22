from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('books/', views.list_books, name="books")
  
]