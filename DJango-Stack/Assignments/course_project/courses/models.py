from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# Bonus: Seperate Description Class
class Description(models.Model):
    content = models.TextField(validators=[MinLengthValidator(15)])
    
    def __str__(self):
        return self.content[:30] # first 30 chars

# Course Class Model:
class Course(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(6)]
    )
    description = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# Comments Class Model:
class Comment(models.Model):
    course = models.ForeignKey(
        Course, 
        related_name='comments', 
        on_delete=models.CASCADE
    )
    content = models.TextField(
        validators=[MinLengthValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.course.name}"