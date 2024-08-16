from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Author, Book, Library, Librarian

# Create your views here.
def list_books(request):
    books = Book.objects.all() #fetching all books from the database
    context = {'list_books':books} #creates a context dictionary with list of books
    return render(request, 'relationship_app/list_books.html', context)




