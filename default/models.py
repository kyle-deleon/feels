from django.db import models
import re
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be two characters long"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be two characters long"
        if len(postData["email"]) < 1:
            errors["email"] = "Email cannot be blank"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter valid email"
        #dont do if len(postData["email"]) < 8
        if postData['bday'] == "":
            errors["bday"] = "Birthday must be filled in"
        date = datetime.strptime(postData["bday"], "%Y-%m-%d")
        if date > datetime.now():
            errors["bday"] = "Birthday cannot be in the future"
        if len(postData["password"]) < 8:
            errors["password"] = "password must be atleast 8 characters long"
        elif postData["password"]

        result = User.objects.filter(email=postData['email'])
        #use .filter over .get if you dont know what the query result will be
        if result:
            errors['email'] = "Email name already in use "

        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    bday = models.DateField()
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<User: {self.id} - {self.first_name} - {self.last_name}>"

    objects = UserManager()
    #connects to class UserManager

class Feels(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User,related_name="feels_created", on_delete="CASCADE")
    liked_by = models.ManyToManyField(User, related_name="liked_feels")


class Comments(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User,related_name="comments_created", on_delete="CASCADE")
    feels = models.ForeignKey(Feels,related_name="has_comments", on_delete="CASCADE")




    




