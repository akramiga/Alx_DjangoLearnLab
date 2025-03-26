from rest_framework import serializers
from.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Post, Comment



class PostSerializer(serializers.ModelSerializer):
    #author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
   # author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
