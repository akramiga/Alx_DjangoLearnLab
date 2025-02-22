from django.shortcuts import render
from django.http import HttpResponse
from .models import Book , Library
from django.views import View
from django.views.generic import ListView
# Create your views here.
#function based view
def list_books(request):
    books = Book.objects.all()
    book_list = ""
    for book in books:
        book_list += f"{book.title} {book.author}"
        return HttpResponse(book_list)
# class basewd view
class LibraryView(ListView):
    model = Library 
    template_name = 'library.html'
    context_object_name = 'libraries'
    def get_queryset(self):
        return self.model.objects.all()   