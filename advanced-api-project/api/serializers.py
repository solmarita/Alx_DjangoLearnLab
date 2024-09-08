from rest_framework import serializers
from .models import Author, Book

# BookSerializer handles serialization of Book instances and includes validation for the publication year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer handles serialization of Author instances and includes nested serialization of related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
