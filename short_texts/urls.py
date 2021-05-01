from django.urls import path
from . import views


app_name = 'short_texts'

urlpatterns = [
	path('', views.api_overview, name='api-overview'),
	path('post/post_details/<int:pk>', views.get_post_details, name='get-post-details'),
	path('post', views.PostsView.as_view(), name='create-post'),
	path('post/<int:pk>', views.PostsView.as_view(), name='update-delete-post'),
]