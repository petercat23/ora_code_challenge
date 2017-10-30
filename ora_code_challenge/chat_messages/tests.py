import json

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


class TestMessages(APITestCase):

    url_create_list_messages = reverse('list_create_message')
    url_session_create = reverse('create_session')

    def setUp(self):
        # get a session token
        response = self.client.post(self.url_session_create)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.access_token = response._headers['authorization'][1]
        self.refresh_token = response._headers['refresh'][1]
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)

        raw_token = self.access_token.split(" ")[-1]
        token = AccessToken(raw_token)

        self.user_id = token['user_id']

    def test_message_create(self):
        data = {
          "data": {
            "type": "messages",
            "attributes": {
              "message": "You gotta go with option 1"
            }
          }
        }
        response = self.client.post(self.url_create_list_messages,
                                    data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content.decode('utf-8'))
        self.assertEqual(result['data']['type'], data['data']['type'])

        data = {
          "data": {
            "type": "messages",
            "attributes": {
              "bad_attribute": "You gotta go with option 1"
            }
          }
        }
        response = self.client.post(self.url_create_list_messages,
                                    data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_message_list_new_refresh_token(self):
        data = {
          "data": {
            "type": "messages",
            "attributes": {
              "message": "You gotta go with option 1"
            }
          }
        }
        response = self.client.post(self.url_create_list_messages,
                                    data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        headers = {'refresh': self.refresh_token}

        response = self.client.get(self.url_create_list_messages, headers=headers,
                                   content_type='application/vnd.api+json')

        # self assert that the new token doesn't equal the old
        self.assertFalse(response._headers['refresh'][1] == self.refresh_token)
        self.assertFalse(response._headers['authorization'][1] == self.access_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_list(self):
        data = {
          "data": {
            "type": "messages",
            "attributes": {
              "message": "You gotta go with option 1"
            }
          }
        }
        response = self.client.post(self.url_create_list_messages,
                                    data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.url_create_list_messages,
                                   content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' not in response._headers)
