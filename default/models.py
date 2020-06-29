from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<User: {self.id} - {self.first_name} - {self.last_name}>"

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
    




