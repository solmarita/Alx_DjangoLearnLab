from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets # Addeded for question 2
from rest_framework.permissions import IsAuthenticated # Added for question 3
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
    permission_classes = [IsAuthenticated]  # Only authenticated users can access



