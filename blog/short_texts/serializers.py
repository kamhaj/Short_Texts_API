''' To make our objects available through the API, we need to perform a serialization – reflect the data 
contained in the object textually. The default format here is JSON, although DRF allows serialization to XML or YAML
'''
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        # model to be serialized
        model = Post 					
        # fields to be displayed
        fields = (
            'title', 
            'content',
            'views_counter')

        read_only_fields = ('pk', 'created_date', 'edition_date', 'views_counter')


    def get(self, post_instance):
        post_instance.update_views_counter()
        return 0


    def update(self, validated_data, post_instance):
        # update post info
        post_instance.title = validated_data.pop('title')
        post_instance.content = validated_data.pop('content')

        # reset views counter and update edition date
        post_instance.reset_views_counter()
        post_instance.update_edition_date()

        # save instance to db
        post_instance.save()
        return post_instance