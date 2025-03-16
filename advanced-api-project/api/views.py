from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class BookListView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fileds = ['title', 'author','publication_year']
    search_fields=['title', 'author']
    odering_fields=['title','publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes =[IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]  
    def create(self, request, *args, **kwargs):
        """Handles book creation and returns a custom response."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()  # Saves the new book instance
            return Response({
                "message": "Book added successfully!",
                "book": BookSerializer(book).data  # Returns serialized book data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]
