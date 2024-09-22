from django.urls import path
from .views import NotificationListView, MarkNotificationsAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications_list'),
    path('mark-read/', MarkNotificationsAsReadView.as_view(), name='mark_notifications_as_read'),
]
