from django.utils.six import text_type

# from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from chat_sessions.models import Session
from users.models import User
# from users.serializers import UserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        try:
            self.user = User.objects.get(username=attrs.get('username', ''))
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'No user found with username `{0}`'.format(attrs.get('username', '')))

        refresh = self.get_token(self.user)

        return {'access': text_type(refresh.access_token)}


class SessionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'

    user = ResourceRelatedField(read_only=True)
