from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.base_user import BaseUserManager 
from django.utils.translation import gettext as _

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    uuid = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    f_name = models.CharField(max_length=512, null=True, blank=True)
    l_name = models.CharField(max_length=512, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=512, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  
  
    objects = CustomUserManager() 


class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uuid = models.UUIDField(null=True, blank=True, default=uuid.uuid4)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # _id = models.CharField(max_length=1024, null=True, blank=True)
    keyword = models.CharField(max_length=1024, null=True, blank=True)
    categories = models.CharField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=1024, null=True, blank=True)
    profile_url = models.CharField(max_length=1024, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)
    city = models.CharField(max_length=1024, null=True, blank=True)
    state = models.CharField(max_length=1024, null=True, blank=True)
    postal_code = models.IntegerField( null=True, blank=True)
    phone = models.CharField(max_length=1024, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=1024, null=True, blank=True)
    rating = models.CharField(max_length=1024, null=True, blank=True)
    review = models.CharField(max_length=1024, null=True, blank=True)
    years_in_business = models.IntegerField(null=True, blank=True)
    bbb_rating = models.CharField(max_length=1024, null=True, blank=True)
    other_links = ArrayField(models.URLField(null=True, blank=True), default=list)

    def __str__(self):
        return "%s"%(self.uuid)
    
    # class Meta:
    #     db_table = "core_details"

class Locations(models.Model):
    state = models.CharField(max_length=512, null=True, blank=True)
    cities = ArrayField(models.CharField(max_length=1024, null=True, blank=True), default=list)

class Categories(models.Model):
    categories_name = models.CharField(max_length=512, null=True, blank=True)
