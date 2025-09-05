from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return f"{self.team_name} ({self.location})"

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"