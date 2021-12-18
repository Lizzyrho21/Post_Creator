from rest_framework import serializers
from . models import *
  
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # Import all fields from model specified  