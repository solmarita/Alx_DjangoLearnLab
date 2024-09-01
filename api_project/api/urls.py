from django.urls import path, include #Added 'include' for question 2
from rest_framework.routers import DefaultRouter
from .views import BookViewSet#,BookListCreate # Uncomment '#,BookListCreate' to answer question 1

# Uncomment this to answer question 1
# urlpatterns = [
#     path('books/', BookListCreate.as_view(), name='book-list-create'),
# ]

# Answer to question 2
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
