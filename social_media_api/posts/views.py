from rest_framework import generics
import rest_framework.permissions as permissions
from rest_framework.response import Response
from posts.models import Post
from accounts.models import CustomUser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from posts.models import Like, Post
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics

# Like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Generate a notification for the post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post,
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

# Unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)

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

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        # Use get_object_or_404 to retrieve the post by primary key or return a 404
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post