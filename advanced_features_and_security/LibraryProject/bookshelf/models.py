from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.contrib.contenttypes.models import ContentType



#Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    class Meta:
        permissions = [
            ('can_create', 'can create'),
            ('can_view', 'can view'),
            ('can_edit', 'can edit'),
            ('can_delete', 'can delete') 
        ]
    
    def __str__(self):
        return self.title
# Create groups

editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Get permissions
content_type = ContentType.objects.get_for_model(Book)
can_view = Permission.objects.get(codename='can_view', content_type=content_type)
can_create = Permission.objects.get(codename='can_create', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)
    # Assign permissions to the groups
editors_group.permissions.add(can_create, can_edit, can_delete)
viewers_group.permissions.add(can_view)
admins_group.permissions.add(can_view, can_create, can_edit, can_delete)   



    
    
#creating acustom user model and adding custom fields
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(unique= False)
   # profile_photo = models.ImageField(upload_to='images/', null= True)
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