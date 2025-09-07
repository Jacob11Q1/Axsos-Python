import re
from django.db import models

# Custom Manager for validation
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # ----------------- Blog Validations -----------------
        if 'name' in postData and len(postData.get('name','')) < 5:
            errors['name'] = "Blog name should be at least 5 characters"
        if 'desc' in postData and len(postData.get('desc','')) < 10:
            errors['desc'] = "Blog description should be at least 10 characters"

        # ----------------- Admin Validations -----------------
        # Email pattern validation
        if 'email' in postData:
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Invalid email address!"

        # First and last name validation (letters only)
        if 'first_name' in postData and not postData['first_name'].isalpha():
            errors['first_name'] = "First name must contain only letters"
        if 'last_name' in postData and not postData['last_name'].isalpha():
            errors['last_name'] = "Last name must contain only letters"

        return errors

# ----------------- Blog Model -----------------
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogManager()  # Link our custom manager

    def __str__(self):
        return self.name

# ----------------- Comment Model -----------------
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

# ----------------- Admin Model -----------------
class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name="admins")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
