'''
Check if invoking a certain URL will trigger given class/view function.
'''

from short_texts.views import *
from django.urls import reverse, resolve
from short_texts.models import Post
from short_texts.views import *


class TestGeneralURLs():

    def test_api_overview_url(self):
        found = resolve(reverse('short_texts:api-overview')) #resolving URL paths to the corresponding view function
        print(found)
        assert found.func == api_overview


class TestPostURLs():

    def test_post_details_url(self):
        found = resolve(reverse('short_texts:get-post-details', kwargs={'pk': '1'}))
        print(found)
        assert found.func == get_post_details

    def test_post_creation_url(self):
        found = resolve(reverse('short_texts:create-post'))
        print(found)
        assert found.func.view_class == PostsView

    def test_post_update_url(self):
        found = resolve(reverse('short_texts:update-delete-post', kwargs={'pk': '1'}))
        print(found)
        assert found.func.view_class == PostsView

    def test_post_deletion_url(self):
        found = resolve(reverse('short_texts:update-delete-post', kwargs={'pk': '1'}))
        print(found)
        assert found.func.view_class == PostsView