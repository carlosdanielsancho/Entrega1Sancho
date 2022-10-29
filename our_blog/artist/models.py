from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=40)
    active = models.CharField(max_length=15)
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Artist: {self.name} | Genre: {self.genre} | Active: {self.active}"
    
