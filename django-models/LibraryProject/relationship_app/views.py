from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Library, Book
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .decorators import is_admin, is_librarian, is_member


#function based view
def list_books(request):
    books = Book.objects.all()
    book_list = ""
    for book in books:
        book_list += f"{book.title} {book.author}"
    return render(request, "relationship_app/list_books.html", {"books": books})    
   # return HttpResponse(book_list)
# class basewd view
class LibraryView(ListView):
    model = Library 
    template_name = 'library_detail.html'
    context_object_name = 'libraries'
    def get_queryset(self):
        return self.model.objects.all()   
    
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Ensure this template exists
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()  # Fetch all books in this library
        return context
    
"""
Setting up User Authentication Views:
Utilize Django’s built-in views and forms for
handling user authentication. 
You will need to create views for user login, logout, and registration.

"""    
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data = request.POST)
#         if form .is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('homme')
#     else:
#         form = AuthenticationForm()   
#     return render(request,'relationship_app/login.html', {'form': form} ) 
class LoginView(LoginView):
    template_name = 'users/login.html'

# def logout_view(request):
#     logout(request)
#     return render(request, 'users/logout.html')
class LogoutView(LogoutView):
    template_name = 'users/logout.html'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('index')  # Redirect to homepage after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


#our role based views
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse('welcome admin')
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse('wecome librarian')
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse('welcome member')