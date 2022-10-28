from django.db import models

# Create your models here.

class Album(models.Model):
    performer = models.CharField(max_length=40)
    title = models.CharField(max_length=60)
    release = models.IntegerField()
    genre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.performer} | {self.title} | {self.release} | {self.genre}"