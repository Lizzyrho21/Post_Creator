from django.urls import path
from .views import *

urlpatterns = [
    path('', ReadAllPosts.as_view(), name="posts"),
    path('<int:pk>/', ReadOnePost.as_view(), name="one_post"),
    path('create/', CreateAPost.as_view(), name="create"),
    path('<int:pk>/update', UpdatePost.as_view(), name="update"),
    path('<int:pk>/delete', DeletePost.as_view(), name="delete"),
    ]