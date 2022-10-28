from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=40)
    active = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name} | {self.genre} | {self.active}"
    
