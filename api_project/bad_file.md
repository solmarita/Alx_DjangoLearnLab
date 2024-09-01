# I'm aware this is bad practice! Just needed a temp file to store this stuff.

{"token":"51a582ad33571a63fd17148ae3c0ba9e5ef255ce"}

User: Sol
Email: officialmokua@gmail.com
Password: @abc123

# To create a user:

Step 1: Create a Superuser (Admin User)
You can create a superuser, which is a user with administrative privileges, using the Django management command. This superuser can then log in and obtain an authentication token.

Run the following command in your terminal:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter a username, email, and password. For example:

Username: admin
Email: admin@example.com
Password: yourpassword
Step 2: Log in with the Superuser to Obtain a Token
Once the superuser is created, you can use the username and password to obtain an authentication token.

For example, if your superuser credentials are:

Username: admin
Password: yourpassword
You can obtain a token using the following curl command:

```bash
curl -X POST -d "username=admin&password=yourpassword" http://127.0.0.1:8000/api/auth/
```

Or you can use Postman to send a POST request to the /api/auth/ endpoint with the same credentials.

Step 3: Use the Token for Authenticated Requests
Once you receive the token, you can use it to authenticate future API requests by including it in the Authorization header like so:

```bash
Authorization: Token <your_token>
```

Additional Note:
If you need additional users with different roles or permissions, you can create them in the Django admin interface (accessible at http://127.0.0.1:8000/admin/) using the superuser account or via the command line with the createsuperuser command.