from django.urls import path
from . import views
from .views import list_books, LoginView, LogoutView
urlpatterns = [
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('books/', list_books, name="books"),
    path('login/', LoginView.as_view(template_name='relationship_app/templates/login/'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'relationship_app/templates/logout/'), name='logout'),
    path('register/', views.register_view, name='register'),
  
]