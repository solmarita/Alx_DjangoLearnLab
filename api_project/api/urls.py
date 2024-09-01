from django.urls import path, include #Added 'include' for question 2
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token # Added this import to answer question 3
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
    path('auth/', obtain_auth_token),  # Endpoint for obtaining a token, answers number 3
    path('', include(router.urls)),
]
