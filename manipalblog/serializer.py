from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Author, Blog, Comment

class AuthorSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('pk','user','blog')


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all(), many=False)
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ('pk','title', 'body','author','comment')



class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=False)
    class Meta:
        model = Comment
        fields = ('pk','body','blog')