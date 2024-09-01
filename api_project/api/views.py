from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets # Added 'viewsets' for question 2
from .models import Book
from .serializers import BookSerializer

# Uncomment this to answer question 1
# class BookListCreate(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


#Answer to question 2
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



