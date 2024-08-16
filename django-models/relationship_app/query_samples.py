
from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.

books = Book.objects.get(author="author.name")
print(books)

#List all books in a library.
library_name = "library.name"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"Books in {library.name}: ")
for book in books:
    print(f" -{book.title}").objects.all()


#Retrieve the librarian for a library
librarian = Librarian.objects.get()
print(librarian)