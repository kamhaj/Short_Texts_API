'''
for Django inbuilt testing set up class to test views
'''

from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TestPostAPISetUp(APITestCase):

    # run before testing
    def setUp(self):
        self.get_post_url = reverse('short_texts:get-post-details', kwargs={'pk': '1'})
        self.create_post_url = reverse('short_texts:create-post')
        self.update_post_url = reverse('short_texts:update-delete-post', kwargs={'pk': '1'})
        self.delete_post_url = reverse('short_texts:update-delete-post', kwargs={'pk': '1'})
        self.fake = Faker()

        self.user_instance = User.objects.create(username='MickyMouse', password='sophisticated-pws-123')
        self.user_token_instance = Token.objects.create(user=self.user_instance)

        self.user_data = {
            'title': self.fake.text(max_nb_chars=60),
            'content': self.fake.text(max_nb_chars=160)
        }


        #self.api_authentication()
        return super().setUp()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_token_instance.key}")

    # run after testing
    def tearDown(self):
        return super().tearDown()