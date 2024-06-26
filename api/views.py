from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer, TagSerializer
from blog.models import Post, Tag
from django.shortcuts import redirect, get_object_or_404



@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/posts'},
        {'GET': '/api/posts/id'},

        {'GET': '/api/tags'},
        {'GET': '/api/tags/id'},
        {'GET': '/api/tags/id/posts'},

        # {'POST': '/api/users/token'},
        # {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getAllPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPostById(request,id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllTags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTagById(request,id):
    tag = Tag.objects.get(id=id)
    serializer = TagSerializer(tag,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPostByTagId(request,id):
    tag = get_object_or_404(Tag, id=id)
    posts = tag.posts.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)
    