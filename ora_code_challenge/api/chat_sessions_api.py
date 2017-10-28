from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from chat_sessions.serializers import DataSerializer
from users.models import User


class SessionCreate(views.APIView):

    permission_classes = (AllowAny,)
    serializer_class = DataSerializer

    def post(self, request, *args, **kwargs):

        # create a user object
        username = "user" + 
        user = User()
        # create a sesson object.

        # associate them

        # create json web token

        #return response

        return Response({}, status=status.HTTP_201_CREATED, content_type="application/vnd.api+json")
