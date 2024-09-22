from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from rest_framework.response import Response

class NotificationListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False).order_by('-timestamp')
        notification_data = [
            {
                'actor': notification.actor.username,
                'verb': notification.verb,
                'timestamp': notification.timestamp,
                'read': notification.read
            }
            for notification in notifications
        ]
        return Response(notification_data)

# Mark all notifications as read
class MarkNotificationsAsReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Notification.objects.filter(recipient=request.user, read=False).update(read=True)
        return Response({'status': 'all notifications marked as read'})
