from typing import Any
from django.shortcuts import render,redirect


# Create your views here.
from .models import Book
def list_books(request):
    books = Book.objects.all() #fetching all books from the database
    context = {'list_books':books} #creates a context dictionary with list of books
    return render(request, 'relationship_app/list_books.html', context)


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_list'] = library.get_books_list()
        return context
    

#Setup User Authentication Views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

#User login view
class LoginView(LoginView):
    template_name = "login.html"

#user logout view
class LogoutView(LogoutView):
    template_name = "logout.html"

#homepage view
def index(request):
    return render(request, "index.html")


