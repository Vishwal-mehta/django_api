from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UsersListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='user-detail'),
    path('posts/', BlogListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('likes/', LikesListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikesDetailView.as_view(), name='like-detail'),
]
