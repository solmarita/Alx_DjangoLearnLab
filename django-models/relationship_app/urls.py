from django.urls import path
from .views import list_books, LibraryDetailView, register, index, LoginView, LogoutView

urlpatterns = [
    path("list_books/", list_books, name = "list_books"),
    path("library_detail/", LibraryDetailView.as_view(), name = "library_detail"),
    path("register", register, name = "register"),
    path("login", LoginView.as_view(), name = "login"),
    path("logout", LogoutView.as_view(next_page="/"), name = "logout"),
    path("", index, name = "index")

]