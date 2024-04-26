from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from .models import Posts
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import PostsSerializer
# Create your views here.


class PostCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class DeletePostView(APIView):
    def delete(self, request, pk):
        post = Posts.objects.get(id=pk)
        print(f" user:{request.user}")
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse("Siz bu post muallifi emassiz")


class ListPostsView(APIView):
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)


class DetailPostView(APIView):
    def get(self, request, pk):
        try:
            post = Posts.objects.get(id=pk)
            serializer = PostsSerializer(post)
            return Response(serializer.data)
        except Posts.DoesNotExist:
            raise Http404


class UpdatePostView(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    def put(self, request, pk):
        post = Posts.objects.get(id=pk)
        serializer = PostsSerializer(post, data=request)
        if serializer.is_valid() and post.author == request.user:
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            message = 'Siz bu post egasi emassiz'
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, content=message)
