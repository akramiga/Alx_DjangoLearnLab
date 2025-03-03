Create
from bookshelf.models import Book
Book.objects.create(title ="1984", author ="George Orwell", publication_year=1949)
output 
    <Book: Book object (1)>  
    <Book: 1984>

Retrieve
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
Output
   1984 George Orwell 1949

Update
book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()
Output  
   book = Book.objects.get(title="Nineteen Eighty-Four")
   print(book.title)
   Nineteen Eighty-Four

Delete
Book.objects.all().delete()
Output
  (1, {'bookshelf.Book': 1})
