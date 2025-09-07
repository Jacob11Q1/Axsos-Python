from django.db import models

# Create your models here.

class TVShow(models.Model):
    title = models.CharField(max_length=255, unique=True)  # unique title
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)  # Optional Bonus

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title