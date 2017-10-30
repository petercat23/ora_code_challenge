from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from chat_messages.models import Message
from chat_messages.serializers import MessageSerializer


from core.decorators import rotate_JWT


class ChatMessageListCreate(generics.ListCreateAPIView):

    queryset = Message.objects.all().order_by('id')  # `order by` for consistent pagination
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )

    @rotate_JWT
    def post(self, request, *args, **kwargs):

        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(user=request.user)

        return Response(self.serializer_class(instance).data,
                        headers=self.headers,
                        status=status.HTTP_201_CREATED,
                        content_type="application/vnd.api+json")

    @rotate_JWT
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
