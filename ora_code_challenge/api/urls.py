from django.conf.urls import url

from api import chat_sessions_api, chat_messages_api

urlpatterns = [
    url(r'^sessions/?$', chat_sessions_api.ChatSessionCreate.as_view(), name="create_session"),
    url(r'^messages/?$', chat_messages_api.ChatMessageListCreate.as_view(), name='list_create_message')
]
