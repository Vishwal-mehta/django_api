from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.permissions import BasePermission,IsAuthenticated,IsAdminUser
from rest_framework import generics, permissions
# Create your views here.

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
       
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if request.method == 'PUT' and request.user.is_authenticated:
            return True
        if request.method in ['PUT', 'DELETE'] and request.user.is_authenticated and request.user.is_staff:
            return True
        return obj.owner == request.user


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]  
    def perform_update(self, serializer):
        
        if serializer.instance.owner == self.request.user or self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionError("You are not allowed to update this post.")

    def perform_destroy(self, instance):
        
        if instance.owner == self.request.user or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionError("You are not allowed to delete this post.")

class LikesListCreateView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class LikesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
