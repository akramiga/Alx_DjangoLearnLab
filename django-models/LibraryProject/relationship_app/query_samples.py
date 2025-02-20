import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  
django.setup()
from relationship_app.models import Library, Librarian, Author, Book

