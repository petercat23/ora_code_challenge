import random
import string

from django.db import transaction
from django.conf import settings

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from chat_sessions.serializers import CustomTokenObtainPairSerializer, SessionsSerializer
from chat_sessions.models import Session
from users.models import User

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class ChatSessionCreate(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = SessionsSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """
        Create a sessions object with a newly create user. Generate a json web
        token based on user and return response.
        """

        # create a user object
        # should be random "enough". Obviously this doesn't guarantee uniqueness
        random_chars = ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(6))
        username = "user" + random_chars

        user = User.objects.create(username=username)

        # create a sesson object.
        session = Session.objects.create(user=user)
        session_serializer = self.serializer_class(session)

        token_serializer = CustomTokenObtainPairSerializer(
            data={'username': user.username, 'password': user.username})

        try:
            token_serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        access = token_serializer.validated_data['access']
        refresh = token_serializer.validated_data['refresh']

        headers = {
            'Authorization': settings.JWT_HEADER_TYPE + access,
            'Refresh': settings.JWT_HEADER_TYPE + refresh
        }

        return Response(session_serializer.data,
                        headers=headers,
                        status=status.HTTP_201_CREATED,
                        content_type="application/vnd.api+json")
