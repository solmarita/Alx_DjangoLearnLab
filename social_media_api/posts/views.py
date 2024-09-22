from rest_framework import generics
import rest_framework.permissions as permissions
from rest_framework.response import Response
from posts.models import Post
from accounts.models import CustomUser

# Feed view to show posts from followed users
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get all users the current user is following
        following_users = request.user.following.all()

        # Filter posts by authors who are in the following list, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Prepare the post data to return
        post_data = [
            {
                'author': post.author.username,
                'content': post.content,
                'created_at': post.created_at
            }
            for post in posts
        ]

        return Response(post_data)
