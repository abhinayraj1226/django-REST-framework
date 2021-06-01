from datetime import date
from functools import partial
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from .models import Author, Blog, Comment
from .serializer import BlogSerializer, AuthorSerializer, CommentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "GET":
        data = Blog.objects.all()

        data_serializer = BlogSerializer(data, many=True)
        print(data_serializer.data)
        data = {
                "status" : "200",
                "data" : data_serializer.data,
            }

        return JsonResponse(data, safe=False)
    else:
            return JsonResponse("error", status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def addUser(request):

    if request.method == "POST":
        author = JSONParser().parse(request)
        author_serializer = AuthorSerializer(data = author)

        if author_serializer.is_valid():
            author_serializer.save()

        return JsonResponse( author_serializer.data, status=status.HTTP_201_CREATED, safe=False)


@csrf_exempt
def postBlog(request):

    if request.method == "POST":
        blog = JSONParser().parse(request)
        blog_serializer = BlogSerializer(data = blog)

        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse( blog_serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse( blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@csrf_exempt
def post_comment(request):
    if request.method == "POST":
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data = comment_data)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse( comment_serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse( comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@csrf_exempt
def deleteComment(request, pk):

    try:
        comment = Comment.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse( "Comment does not exist", status=status.HTTP_404_NOT_FOUND, safe=False)
    if request.method == "GET":
        comment_serializer = CommentSerializer(comment)
        return JsonResponse( comment_serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == "DELETE":
        comment.delete()
        return JsonResponse( "Comment deleted", status=status.HTTP_200_OK, safe=False)


@csrf_exempt
def updateBlog(request, pk):

    blog_data = JSONParser().parse(request)
    blog = Blog.objects.get(pk=pk)

    blog_serializer = BlogSerializer(blog, data=blog_data, partial=True)

    if blog_serializer.is_valid():
        blog_serializer.save()
        return JsonResponse(blog_serializer.data, status=status.HTTP_200_OK, safe=False)
    return JsonResponse(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    # try:
    #     bl = Blog.objects.get(title=pk)
    #     blog = BlogSerializer(bl ,data = {"body" : rblog['body']}, partial=True)
    #     if blog.is_valid():
    #         blog.save()
    #     return JsonResponse('ok', status=status.HTTP_200_OK, safe=False)
    # except:
    #     return JsonResponse('error', status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    
    




