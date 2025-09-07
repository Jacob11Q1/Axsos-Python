from django.db import models

# Create your models here.

class TVShow(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title