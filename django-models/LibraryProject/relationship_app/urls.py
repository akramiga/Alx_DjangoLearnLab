from django.urls import path
from . import views
urlpatterns = [
    path('library/', views.LibraryView.as_view(), name='library'),
    path('books/', views.list_books, name="books")
  
]