from django.db import models

# Create your models here.


class Post(models.Model):
    word = models.CharField(max_length=10000)

    def __str__(self):
        return self.word
