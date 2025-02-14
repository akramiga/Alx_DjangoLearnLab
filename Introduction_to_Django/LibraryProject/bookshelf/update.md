Update
book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()
Output  
   book = Book.objects.get(title="Nineteen Eighty-Four")
   print(book.title)
   Nineteen Eighty-Four

