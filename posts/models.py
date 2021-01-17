from django.db import models

# Create your models here.

class Post(models.Model):

    summary = models.TextField()

    def __str__(self):
        return self.summary