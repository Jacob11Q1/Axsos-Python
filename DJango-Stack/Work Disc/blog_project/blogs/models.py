from django.db import models

# Create your models here.

# Custom Manager for Blog
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData.get('name', '')) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData.get('desc', '')) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors

class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = BlogManager() # Limking custom manager
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name="admins")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
