'''
unit tests examples for testing models
testing models is basically checking if we can work with the model (CRUD operations)
if some default methods (e.g. save()) were overridden, then they should be tested too
'''

#from django.test import TestCase
from short_texts.models import Post
from .factories import PostFactory
import pytest


@pytest.mark.django_db
class TestPostModel():   

    def test_create_new_program(self):
        post = PostFactory()
        # Check all field and validators
        post.clean_fields()  #  EXCLUDE: FK, O2O, M2M Fields
        
        # Check we can find it
        posts = Post.objects.all()
        assert len(posts) == 1

        first_post = posts[0]
        assert first_post == post


    @pytest.mark.django_db
    def test_check_attribute_in_program(self):
        # Check attributes
        post = PostFactory()
        assert post.title == 'Test Post Title'
        assert post.content == 'Test content.'
        assert post.views_counter == 0


    @pytest.mark.django_db
    def test_check_str_representation_of_program(self):
        # Check string representation
        post = PostFactory(title="New Post Title", content='New content.')
        assert post.__str__() == 'New Post Title'