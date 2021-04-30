from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.decorators import api_view 	# function based views API
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from rest_framework import status

from .serializers import PostSerializer
from .models import Post

#from django.shortcuts import render, HttpResponse
# from django.db import IntegrityError
# from rest_framework import status
# import json
# from rest_framework.permissions import IsAuthenticated

'''
dodaj uwierzytelnianie (oprocz metody GET)


'''

# def views_counter(request, id):
#     ## refresh views and save
#     post_object = Post.objects.get(id=id)
#     post_object.views_counter = post_object.views_counter + 1
#     post_object.save()



@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'GET post details': '/post/<int:pk>/',
		'POST (create) post': '/post/',
		'PUT (update) post': '/post/<int:pk>/',
		'DELETE post:': '/post/<int:pk>/'
	}

	# return API response
	return Response(api_urls)


'''
    {  
        "title": "Test Post 3 Updated",
        "content": "Lorem ipsum three updated."
    }
'''
class PostsView(APIView):

	## get object or 404
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404()


    ## get all objects from db
    def get(self, request, pk, format=None):
        post_instance = self.get_object(pk)
        serializer = PostSerializer(post_instance)
        serializer.get(post_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    ## create one object
    def post(self, request, format=None):
        # serialize user input
        serializer = PostSerializer(data=request.data)
        # validate user input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    ## update one object
    def put(self, request, pk, format=None):
        # serialize user input
        serializer = PostSerializer(data=request.data)
        # validate user input, save changes to db if ok, return errors if not
        if serializer.is_valid():
            post_instance = get_object(pk)
            serializer.update(request.data, post_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    ## delete one object
    def delete(self, request, pk, format=None):
        post_instance = self.get_object(pk)
        post_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
