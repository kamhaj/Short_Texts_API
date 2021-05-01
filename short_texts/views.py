from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from rest_framework import status

from .serializers import PostSerializer
from .models import Post

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'GET post details': '/api/short_texts/post/get_post_details/<int:pk>/',
		'POST (create) post': '/api/short_texts/post/',
		'PUT (update) post': '/api/short_texts/post/<int:pk>/',
		'DELETE post:': '/api/short_texts/post/<int:pk>/'
	}

	# return API response
	return Response(api_urls)


## get one Post objects from db
@api_view(['GET'])
def get_post_details(request, pk):
    post_instance = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post_instance)
    serializer.get(post_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)



class PostsView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]		# will deny permission to any unauthenticated user

    ## get object or 404
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404()


    ## create one object, required attributes are: title, content
    def post(self, request, format=None):
        # serialize user input
        serializer = PostSerializer(data=request.data)
        # validate user input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    ## update one object, required attributes are: title, content
    def put(self, request, pk, format=None):
        # serialize user input
        serializer = PostSerializer(data=request.data)
        # validate user input, save changes to db if ok, return errors if not
        if serializer.is_valid():
            post_instance = self.get_object(pk)
            serializer.update(request.data, post_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    ## delete one object
    def delete(self, request, pk, format=None):
        post_instance = self.get_object(pk)
        post_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
