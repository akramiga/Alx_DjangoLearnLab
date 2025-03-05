from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name='books')
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=120)
    books = models.ManyToManyField(Book, related_name='library') 
    def __str__(self):
        return self.name 

class Librarian(models.Model):
    name = models.CharField(max_length=120)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name          

#user profilr model
class UserProfile(models.Model):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),

    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    role = models.CharField(max_length=20, choices = ROLE_CHOICES)
    def __str__(self):
        return f"{self.user.username} ({self.role})"

#signal to create profile automatically
@receiver(post_save, sender = User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)    
@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.userprofile.save()        

