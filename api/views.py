from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from api.models import Post
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#actions need to change too upvote and downvote instead of boast and roast
    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(boast_or_roast=True).order_by('-date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(boast_or_roast=False).order_by('-date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
    @action(detail=False)
    def highestvotes(self, request):
        highestvotes = Post.objects.all().order_by('downvotes', '-upvotes')
        seriallizer = self.get_serializer(highestvotes, many=True)
        return Response(seriallizer.data)

    @action(detail = True, methods=['post'])
    def upvote(self, request, id):
        post = Post.objects.get(id=id)
        post.upvote += 1
        post.save()
        return Response('success')

    @action(detail= True, methods=['post'])
    def downvote(self, request, id):
        post = Post.objects.get(id=id)
        post.downvote += 1
        post.save()
        return Response('success')

   

   
