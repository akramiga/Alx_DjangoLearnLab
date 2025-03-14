from django.db import models

# Create your models here.



'''
author model to store details about the authors of the books,
 the name of the author, limited to 300 characters
 and a string representation of the Author object to display the name
'''
class Author(models.Model):
    name = models.CharField(max_length= 300)
    def __str__(self):
        return self.name



'''
book model to store details about books.
the title of the book, limited to 300 characters.
the year the book was published. this will store the year as an integer.
'''
class Book(models.Model):
    title = models.CharField(max_length= 300)
    publication_year = models.IntegerField()
    '''
    foreign key relation to the author model. 
  this creates a relationship where each book is associated with one author.
'''
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return f"{self.title} by {self.author}"

