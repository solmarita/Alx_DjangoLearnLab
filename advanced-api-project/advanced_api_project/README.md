## API Endpoints

- **List Books:** `GET /books/` - Retrieve all books.
- **Create Book:** `POST /books/` - Create a new book.
- **Retrieve Book:** `GET /books/<int:pk>/` - Retrieve a specific book by ID.
- **Update Book:** `PUT /books/<int:pk>/` - Update a specific book by ID.
- **Delete Book:** `DELETE /books/<int:pk>/` - Delete a specific book by ID.

### Permissions

- List and Retrieve endpoints are accessible to all users.
- Create, Update, and Delete endpoints are restricted to authenticated users.
