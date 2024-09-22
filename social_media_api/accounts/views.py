from rest_framework import generics, status
import rest_framework.permissions as permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser

# Follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        if target_user != request.user:
            request.user.following.add(target_user)
            return Response({'status': 'followed'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = CustomUser.objects.all()
        if target_user != request.user:
            request.user.following.remove(target_user)
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
