from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


from chat_messages.models import Message
from chat_messages.serializers import MessageSerializer


class ChatMessageListCreate(generics.ListCreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save(user=request.user)

        # TODO still need to rotate json web token
        return Response(self.serializer_class(instance).data,
                        headers={'Authorization': request.META['HTTP_AUTHORIZATION']},
                        status=status.HTTP_201_CREATED,
                        content_type="application/vnd.api+json")

    #  def list(self, request, *args, **kwargs):
