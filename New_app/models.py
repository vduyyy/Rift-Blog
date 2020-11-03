from __future__ import unicode_literals
from django.db import models
import bcrypt
import re


Email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors ={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters long"
        
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters long"
        
        if len(postData['user_name']) < 2:
            errors['user_name'] = "Last Name must be at least 2 characters long"
        
        if User.objects.filter(user_name = postData['user_name']).exists():
            errors['user_nameexists'] = "User Name already exists!"
        
        if len(postData['password']) <3:
            errors['password'] = "Password is too weak"
        if User.objects.filter(email = postData['email']).exists():
            errors['emailexists'] = "Email already exists!"
        
        if not Email_regex.match(postData['email']):
            errors['email']= "Invalid email address"
        return errors
    
    def login_validator(self, postData):
        if not Email_regex.match(postData['email']):
            errors['email']= "Invalid email address"
        return errors



class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    user_name = models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Path(models.Model):
    title = models.CharField(max_length = 255)
    champion=models.CharField(max_length=255)
    build = models.CharField(max_length=255)
    lane = models.CharField(max_length=100)
    user_upload = models.ForeignKey(User, related_name="uploaded_by", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Message(models.Model):
    message = models.TextField()
    user= models.ForeignKey(User, related_name='user_message', on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    objects = UserManager()