from django.db import models
from accounts.models import CustomUser


# Create your models here.
'''
In a new app within the project called posts, create models for Post and Comment.
Post should have fields like author (ForeignKey to User), title, content, created_at, and updated_at.
Comment should reference both Post (ForeignKey) and User (author), with additional
 fields for content, created_at, and updated_at.'''

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} '