from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= "__all__"# Include all fields of the Book model

     
     # Validation method to check the publication year of the book.
    def validate(self, data):
        publication_year = data.get('publication_year')

        # Ensure that a publication year is provided.
        if publication_year is None:
            raise serializers.ValidationError("PUBLICATION YEAR IS REQUIRED") 
        
        '''
        get the current year and
        check if the publication year is in the future
        '''
        year = timezone.now().year
        if publication_year  > year:
            raise serializers.ValidationError("YEAR CANNOT BE  A FUTURE DATE")  
        return data
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']        

'''
In the AuthorSerializer 
the relationship between the Author and Book models is handled by including the books field
which is a nested BookSerializer. This creates a one-to-many relationship, 
meaning that each author can have multiple books. 
By setting many=True in the books field,
you ensure that the serializer can handle multiple book objects associated with the author
'''        