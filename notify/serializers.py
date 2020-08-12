from rest_framework import serializers
from notify.models import Notification, STATUS_CHOICE

class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('date', 'time', 'message', 'status')

