from django.conf.urls import url

from api import chat_messages_api, chat_sessions_api

urlpatterns = [
    url(r'^sessions/?$', chat_sessions_api.SessionCreate.as_view(), name="create_session")
    # url(r'^user/sessions/?$', users_api.UserLogin.as_view(), name='login'),
]
