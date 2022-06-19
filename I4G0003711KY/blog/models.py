from tkinter import CASCADE
from typing import Any
from typing_extensions import Self
from django.db import models
from typing_extensions import Self
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Post (models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField('created_date')
    Published_date = models.DateTimeField('published_date')
    def __str__(self) -> str:
        return super().__str__()
    
    
