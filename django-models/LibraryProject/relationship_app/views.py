from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Library, Book
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import permission_required,user_passes_test
from .decorators import is_admin, is_librarian, is_member
from django import forms
from.models import UserProfile


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
# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == UserProfile.ADMIN

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == UserProfile.LIBRARIAN

def is_member(user):
    return user.userprofile.role == UserProfile.MEMBER


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')
    #return HttpResponse('welcome admin')
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')
    #return HttpResponse('wecome librarian')
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')
    #return HttpResponse('welcome member')

#
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

# View to add a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View to edit an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})