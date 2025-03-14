from rest_framework.serializers import ModelSerializer
from core.models import ScraperFile, Notifications

class ScraperFileSerializer(ModelSerializer):
    class Meta:
        model = ScraperFile
        fields = ['id', 'owner', 'file_id', 'name', 'created_on']


class NotificationsSerializer(ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['owner', 'document', 'header', 'body', 'file_id']