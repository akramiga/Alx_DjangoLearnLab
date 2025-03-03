from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
    
#creating acustom user model and adding custom fields
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(unique= False)
    profile_photo = models.ImageField(upload_to='images/', null= True)
    def __str__(self):
        return self.username
#custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email:
            return ValueError('PLEASE ADD EMAIL')
        user = self.model(email= self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self, email, password = None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    