from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import PostSerializer
from api.models import Post
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer