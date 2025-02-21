import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  
django.setup()
from relationship_app.models import Library, Librarian, Author, Book

def list_books(library_name):
    return Library.objects.get(name=library_name).books.all()

def books_by_author(name):
    return Book.objects.filter(author = name)

