
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


from chat_sessions.models import Session

from users.models import User


class SessionsTest(APITestCase):

    url_session_create = reverse('create_session')

    def test_session_create(self):
        response = self.client.post(self.url_session_create)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # assert that a sessions object and user object were created
        self.assertTrue(Session.objects.filter(id=response.data['id']).exists())
        self.assertTrue(User.objects.filter(id=int(response.data['user']['id'])).exists())

        # get the json web token
        full_token = response._headers['authorization'][1]
        raw_token = full_token.split(" ")[-1]
        token = AccessToken(raw_token)

        # get the user id from the payload...
        user_id = token['user_id']

        # assert that the user_id matches the user created in the response
        self.assertEqual(user_id, int(response.data['user']['id']))

        # content holds parsed data
