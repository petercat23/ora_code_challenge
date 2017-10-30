from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from chat_messages.models import Message

from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):

    included_serializers = {
        'user': UserSerializer,
    }

    message = serializers.CharField(required=True)
    user = ResourceRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'user', 'message', 'created', 'modified')

    class JSONAPIMeta:
        included_resources = ['user']
