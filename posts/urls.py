from django.urls import path
from .views import ReadAllPosts

urlpatterns = [path('', ReadAllPosts.as_view(), name="posts"),

]