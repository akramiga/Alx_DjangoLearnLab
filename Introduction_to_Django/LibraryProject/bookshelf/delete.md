
from bookshelf.models import Book
Book.objects.all().delete()
Output
  (1, {'bookshelf.Book': 1})