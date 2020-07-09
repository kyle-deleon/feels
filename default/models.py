from django.db import models
import re
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
        result = User.objects.filter(user_name=postData['email'])
        #use .filter over .get if you dont know what the query result will be
        if result:
            errors['email'] = "Email name already in use "

        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    user_name = models.CharField(max_length=255)
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




    




