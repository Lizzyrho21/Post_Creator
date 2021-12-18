from django.shortcuts import render
from rest_framework import generics #generic methods import from framework
from .serializers import PostSerializer # import JSON serializer!
from .models import Post

# Create your views here.

# read all posts
class ReadAllPosts(generics.ListAPIView):
    queryset = Post.objects.all() # A QuerySet represents a collection of objects from your database
    serializer_class = PostSerializer # Pulling in our serializer to translate into JSON data


# Read one post
class ReadOnePost(generics.RetrieveAPIView):
    queryset = Post.objects.all() # A QuerySet represents a collection of objects from your database
    serializer_class = PostSerializer # Pulling in our serializer to translate into JSON data

# Create a post
class CreateAPost(generics.ListCreateAPIView):
    queryset = Post.objects.all() # A QuerySet represents a collection of objects from your database
    serializer_class = PostSerializer # Pulling in our serializer to translate into JSON data

# Update a post
class UpdatePost(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all() # A QuerySet represents a collection of objects from your database
    serializer_class = PostSerializer # Pulling in our serializer to translate into JSON data

# Delete a post
class DeletePost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all() # A QuerySet represents a collection of objects from your database
    serializer_class = PostSerializer # Pulling in our serializer to translate into JSON data




