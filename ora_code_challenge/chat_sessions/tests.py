
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class SessionsTest(APITestCase):

    url_session_create = reverse('create_session')

    def setUp(self):
        print("HERE???")
        return super().setUp()

    def test_session_create(self):
        response = self.client.post(self.url_session_create)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
