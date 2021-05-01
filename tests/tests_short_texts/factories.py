'''
per app file to store factories
'''

from short_texts.models import Post
import factory


class PostFactory(factory.django.DjangoModelFactory):
   
    class Meta:
        model = Post

    title = 'Test Post Title'
    content = 'Test content.'