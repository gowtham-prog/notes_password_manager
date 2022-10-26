from pickle import TRUE
from django.contrib.auth.models import AbstractUser,User
from django.db import models
import datetime
from fernet_fields import EncryptedTextField

#username, email, password, 
class User(AbstractUser):
    pass
    def __str__(self):
        return f"{self.id}--{self.username}"

# Create your models here.
class Notes(models.Model):
    content=models.TextField(max_length=10000)
    Title=models.CharField(max_length=64)
    owner= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Wishlist= models.BooleanField(default = False)
    def __str__(self):
        return f"{self.id}-{self.Title}- {self.owner}"
class Passwords(models.Model):
    Website=models.CharField(max_length=1000)
    Username= models.CharField(max_length=64)
    Password = EncryptedTextField()
    Key= models.CharField(max_length=512)
    Owner= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.id} -- {self.Username} -- {self.Website}--{self.Key}--"