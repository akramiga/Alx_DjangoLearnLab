from django.urls import path
from . import views
from .views import list_books, LoginView, LogoutView, admin_view, librarian_view, member_view
urlpatterns = [
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('books/', list_books, name="books"),
   # path('login/', LoginView.as_view(template_name='relationship_app/templates/login/'), name='login'),
   # path('logout/', LogoutView.as_view(template_name='relationship_app/templates/logout/'), name='logout'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('register/', views.register_view, name='register'),
    path('admin_dashboard/', admin_view, name='admin_dashboard'),
    path('librarian_dashboard/',librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', member_view, name='member_dashboard'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book', views.delete_book, name='delete_book'),
  
]