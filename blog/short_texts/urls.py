from django.urls import path
from . import views


app_name = 'short_texts'

urlpatterns = [
	path('', views.api_overview, name='api-overview'),
	path('post/get_post_details/<int:pk>', views.get_post_details, name='post-details'),
	path('post/<int:pk>', views.PostsView.as_view(), name='create-update-delete'),
]