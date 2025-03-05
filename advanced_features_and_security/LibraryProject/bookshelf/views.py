from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
@permission_required("book_list", raise_exception= 'books')



@permission_required('bookshelf.can_create', raise_exception=True)
def create(request):
    pass
@permission_required('bookshelf.can_view', raise_exception=True)
def view(request):
    pass
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit(request):
    pass
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete(request):
    pass