from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.
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