from .test__setup import TestPostAPISetUp
from rest_framework import status


class TestPostViews(TestPostAPISetUp):

    ## Test GET
    ## TODO - test_user_cannot_get_post_with_no_data (pk)
    ## TODO - test_user_can_get_post_with_data
    
    ## Test POST
    def test_user_cannot_create_post_with_no_data(self):
        response = self.client.post(self.create_post_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_cannot_create_post_with_no_authentication(self):
        response = self.client.post(self.create_post_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_create_post_with_data_and_authentication(self):
        self.api_authentication()
        response = self.client.post(self.create_post_url, self.user_data, format='json')
        self.assertEqual(response.data['title'], self.user_data['title'])
        self.assertEqual(response.data['content'], self.user_data['content'])
        self.assertEqual(response.data['views_counter'], 0)
        #import pdb
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    ## Test PUT
    ## TODO - test_user_cannot_update_post_with_no_data (pk, title, content)
    ## TODO - test_user_cannot_update_post_with_no_authentication (token)
    ## TODO - test_user_can_update_post_with_data_and_authentication 

    ## Test DELETE
    ## TODO - test_user_cannot_delete_post_with_no_data (pk)
    ## TODO - test_user_cannot_delete_post_with_no_authentication (token)
    ## TODO - test_user_can_delete_post_with_data_and_authentication