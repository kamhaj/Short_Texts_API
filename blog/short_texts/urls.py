from django.urls import path
from . import views


app_name = 'short_texts'

urlpatterns = [
	path('', views.api_overview, name='api-overview'),
	path('post/<int:pk>', views.PostsView.as_view(), name='post-create-update-delete'),
]