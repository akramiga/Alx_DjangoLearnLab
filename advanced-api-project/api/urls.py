from api import views
from django.urls import path

urlpatterns = [
    path('/books/list/', views.BookListView.as_view(), name='book_list'),
    path('/books/<int:pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('/books/create/', views.BookCreateView.as_view(), name='create_book'),
    path('/books/update/', views.BookUpdateView.as_view(), name='update_book'),
    path('/books/delete/', views.BookDeleteView.as_view(), name='delete_book'),
]