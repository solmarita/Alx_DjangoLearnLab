from django.urls import path
from .views import list_books, LibraryDetailView, index, LoginView, LogoutView
from . import views
urlpatterns = [
    path("list_books/", list_books, name = "list_books"),
    path("library_detail/", LibraryDetailView.as_view(), name = "library_detail"),
    path("register", views.register, template_name = "register"),
    path("login", LoginView.as_view(), template_name = "login"),
    path("logout", LogoutView.as_view(next_page="/"), template_name = "logout"),
    path("", index, template_name = "index")

]